
from datetime import date, datetime, timedelta, time
from math import inf
import numpy as np

from api.option_chain import get_option_chain
from processors.vix_processors import combine_contract_data
from constants.contracts import CALL, PUT

MINUTES_PER_MONTH = 60 * 24 * 30
MINUTES_PER_YEAR = 60 * 24 * 365

# An option is standard if its dte falls on the third friday of a month
def get_is_standard(dte):
    expiry_date = date.today() + timedelta(days=dte)
    return expiry_date.weekday() == 4 and 15 <= expiry_date.day <= 21

def T(dte):
    current_day_timedelta = datetime.combine(date.today() + timedelta(days=1), time()) - datetime.now()
    M_current_day = current_day_timedelta.seconds // 60

    M_settlement_day = 570 if get_is_standard(dte) else 960
    M_other_days = 60 * 24 * (dte - 1)

    return (M_current_day + M_settlement_day + M_other_days) / MINUTES_PER_YEAR

def F(strike, r, t, call_price, put_price):
    return strike + np.exp(r*t) * (call_price - put_price)

def K_0(F, strikemap):
    sorted_strikes = sorted(strikemap.keys())
    next_strike_under = 0

    for strike in sorted_strikes:
        if strike > F:
            return next_strike_under
        next_strike_under = strike

    return next_strike_under
    
# Returns the strike with the smallest price difference between calls and puts
def smallest_difference(strikemap):
    smallest_diff = inf
    diff_info = {}

    for strike in strikemap:
        if not (CALL in strikemap[strike] and PUT in strikemap[strike]):
            continue

        call, put = strikemap[strike][CALL], strikemap[strike][PUT]
        call_midpoint = (call['bid'] + call['ask']) / 2
        put_midpoint = (put['bid'] + put['ask']) / 2

        abs_diff = abs(call_midpoint - put_midpoint)
        if abs_diff < smallest_diff:
            smallest_diff = abs_diff
            diff_info = {'strike': strike, 'call_price': call_midpoint, 'put_price': put_midpoint}
    
    return diff_info

def get_otm_options(k_0, contract_type, strikemap):
    options = []

    strike_filter = (lambda s: s > k_0) if contract_type == CALL else (lambda s: s < k_0)
    contract_filter = lambda s: contract_type in strikemap[s]
    sorted_strikes = list(filter(lambda s: strike_filter(s) and contract_filter(s), sorted(strikemap.keys())))

    seen_zero_bid = False

    for strike in sorted_strikes:
        option = strikemap[strike][contract_type]
        if option['bid'] > 0:
            seen_zero_bid = False
            options.append(option)
        elif seen_zero_bid:
            return options
        else:
            seen_zero_bid = True

    return options

# We use k0 as both a call and put option in our K_i's, so we need to take an average of the prices 
def merge_k0(k0, strikemap):
    call_k0 = strikemap[k0][CALL]
    put_k0 = strikemap[k0][PUT]

    return {'bid': (call_k0['bid'] + put_k0['bid']) / 2, 'ask': (call_k0['ask'] + put_k0['ask']) / 2, 'strikePrice': k0}

def sigma_squared(t, r, f, k_0, K_i):
    # Create a list of delta k_i's before the loop so we don't have to specify edge cases there
    delta_k_i = [K_i[1]['strikePrice'] - K_i[0]['strikePrice']]
    delta_k_i.extend([(K_i[i+1]['strikePrice'] - K_i[i-1]['strikePrice']) / 2 for i in range(1, len(K_i) - 1)])
    delta_k_i.extend([K_i[-1]['strikePrice'] - K_i[-2]['strikePrice']])

    k_i_sum = sum((delta_k_i[i] / K_i[i]['strikePrice']**2) * np.exp(r*t) * ((K_i[i]['bid'] + K_i[i]['ask']) / 2) for i in range(len(K_i)))

    return (2 / t) * k_i_sum - (1 / t) * (f / k_0 - 1)**2

def vix(symbol):
    data, _ = get_option_chain(symbol, low_dte=23, high_dte=37, min_volume=0)
    dte_map = combine_contract_data(data[CALL], data[PUT])

    # Initialize our variables
    t1, t2 = None, None
    sigma1, sigma2 = None, None


    # Generalizes to any number of expiration periods
    for dte, strikemap in dte_map.items():
        # Step 0: Find T and R
        if t1:
            t = t2 = T(dte)
        else:
            t = t1 = T(dte) 

        r = 0.016 # TODO: Find a way to get this dynamically

        # Step 1: Find F
        smallest_diff_info = smallest_difference(strikemap)
        f = F(smallest_diff_info['strike'], r, t, smallest_diff_info['call_price'], smallest_diff_info['put_price'])
        
        # Step 2: Find K_0
        k_0 = K_0(f, strikemap)

        # Step 3: Find K_i's
        K_i = get_otm_options(k_0, PUT, strikemap) + [merge_k0(k_0, strikemap)] + get_otm_options(k_0, CALL, strikemap)

        # Step 4: Find sigma^2
        if sigma1:
            sigma2 = sigma_squared(t, r, f, k_0, K_i)
        else:
            sigma1 = sigma_squared(t, r, f, k_0, K_i)
    
    # Step 5: Take square root of 30 day weighted average of each sigma squared
    weighted_avg = (t1 * sigma1 * ((t2 * MINUTES_PER_YEAR - MINUTES_PER_MONTH) / (t2 * MINUTES_PER_YEAR - t1 * MINUTES_PER_YEAR)) + \
                   t2 * sigma2 * ((MINUTES_PER_MONTH - t1 * MINUTES_PER_YEAR) / (t2 * MINUTES_PER_YEAR - t1 * MINUTES_PER_YEAR))) * (MINUTES_PER_YEAR/MINUTES_PER_MONTH)

    return 100 * (weighted_avg**0.5)


        
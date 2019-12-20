from tdameritrade import TDClient
import numpy as np

from scipy.stats import norm

from util import compute_profit_rank

from functools import reduce
import pickle
import os
from os import path
import json

# This token has expired by now, so don't bother using it :)
TOKEN = 'bpdvIrzbkuN0MREt0ogwl/AJNaUn+OKtf/r8oJqlQ7jWzFRP/G54PnFvvAxaE0VMSOqIK9ASMtYxIloQk6eXEJaEzKW2TP9VUG+BM/e3EJ/IduUwh+dTCH9LYOIHDCYTQrWVsV92qWjbt9OlPNuyeTw0+H49bSxP8tzlAwqdXccZ/5UPckNmVS7zZRc/Q8ghYGx6zmEumwwwtlVi+ljJb2NPG+lqMI2M3E9oV/A5ZaCPSLEkbIu3S8Uw2rKQptzl7Y4rQNJgCT/ascR1XxdtkqtceX3O9C+ArkFe+LaOJChFAr+qIaVIYeKhiMQG0E9+6IGTUR+GlMqmNJwgSS/BqaJeZymRYGjWpsBINjVoV8YDVqGbAeOfSSJjKSpeTUsWuh9TE2SmwqAUsaTf7PfF2R1BsNyl1AIwJ18h1EWheqGW9FeyT7jTNlq1rPAA1jaMM8SRlT5On8jOLUC2Rp2PHhUO9oVkfeIUsaEVNUzctn0eSDq9W51WEb2pbo2fE7htavcbz/bNTk7Qggeajp4haxhOAAo+Y2PZWUQKTcf87TE6TmDXK100MQuG4LYrgoVi/JHHvlKYy/9CJkXiPrWxyxITukX+kyKHH/wmIwyFVfkFbtWBBT5yqicOCtb03h936trZxTyWxdbGj6g7rim5SyBRcY4c8jKCQbOtlrjUg6syOEd2tq8rxhe8e/OYhxJyDZ4bZ5fxpaTm55HUD0DzZyyA0r/vv6FSyWYPgu8XTE8vHXQAAY/d1G4jD9vDTmZWaQVYBDCOe3IQu88L3r+8Q/DeRD/DCm+/0PNT0GUWLlqp1P29k6ppTa9ZmPXY8jLGBNb1ymbeAGBET6BIGBLhB4WNae4aR3Bv1+FJrzGnd8L4JxphhRxTFl8Lv9hAnMCfGiug7Bvwf3BGrdloHBMAwbJKSvfidaz+ySYuV3V0uc9LTsv03g1HEavaHurjA1IEftu0pHGt2wW7E+/r+nTOhUCFOxWtYJipYY+Q4RTEuqb9PjEeIs5VDfA0O+qtkzSZqFJgHyOT5KL37y5D+wBFAFPf4RnVZ3rtuIGw68QxTn/oaDRsN3EuRoeZUYhM7POiRYGNZjY4OXAt0El4B+rp9e8ZcycGgCjQCrU+ouTeViauB6QK49hh2Q==212FD3x19z9sWBHDJACbC00B75E'

c = TDClient(TOKEN)

def load_pickle(filename, load_action):
    if path.exists(filename):
        obj = pickle.load(open(filename, 'rb'))
        return load_action(obj)

    return None

def normalize_roi(roi):
    return np.exp(-10 * (roi - 1.5)**2)

def calculate_daily_volatility(symbol):
    def get_volatility(volatilities):
        if symbol in volatilities:
            return volatilities[symbol]

    volatility = load_pickle('volatilities.pickle', get_volatility)
    if volatility:
        return volatility

    volatilities = {}

    candles = c.history(symbol, periodType='year', period='1', frequencyType='daily')['candles']
    price_deltas = [candle['close']/candle['open'] - 1 for candle in candles]

    volatilities[symbol] = np.std(price_deltas)
    pickle.dump(volatilities, open('volatilities.pickle', 'wb'))
    return volatilities[symbol]

def get_last_price(symbol):
    def get_price(prices):
        if symbol in prices:
            return prices[symbol]
    
    price = load_pickle('prices.pickle', get_price)
    if price:
        return price

    last_prices = {}

    last_price = c.quote(symbol)[symbol]['lastPrice']
    last_prices[symbol] = last_price
    pickle.dump(last_prices, open('prices.pickle', 'wb'))
    return last_price

def get_expected_profit(symbol, max_profit, max_loss, high_strike, low_strike):
    daily_volatility = calculate_daily_volatility(symbol)
    last_price = get_last_price(symbol)

    RV = {'loc': last_price, 'scale': (32**0.5) * daily_volatility * last_price}

    p_below, p_above = norm.cdf(low_strike, **RV), (1 - norm.cdf(high_strike, **RV))
    p_between = 1 - p_above - p_below

    return p_below * - max_loss + p_between * (max_profit - max_loss) + p_above * max_profit

def get_vertical_spreads(symbol, contract_type):
    spreads = []

    try:
        strategy_data = pickle.load(open('options.pickle', 'rb'))[symbol][contract_type]
    except:
        strategy_data = c.options(symbol, strategy='VERTICAL', contractType=contract_type)['monthlyStrategyList']
        pickle.dump({symbol: {contract_type: strategy_data}}, open('options.pickle', 'wb'))

    return strategy_data
    
    for expiry_month in strategy_data:
        month_label = '{} {} {}'.format(expiry_month['month'], expiry_month['day'], expiry_month['year'])
        monthly_strategies = expiry_month['optionStrategyList']

        for strategy in filter(lambda strategy: strategy['strategyBid'] > 0, monthly_strategies):
            high_strike, low_strike = strategy['primaryLeg']['strikePrice'], strategy['secondaryLeg']['strikePrice']

            max_profit = ((strategy['strategyBid'] + strategy['strategyAsk']) / 2) * 100
            max_loss = (high_strike - low_strike) * 100 - max_profit

            if max_loss == 0:
                continue

            roi = max_profit / max_loss
            expected_profit = get_expected_profit(symbol, max_profit, max_loss, high_strike, low_strike)
            profit_rank = compute_profit_rank(expected_profit, max_profit)

            strike_spread = {'strikes': strategy['strategyStrike'],
                             'max_profit': max_profit,
                             'max_loss': max_loss,
                             'roi': roi,
                             'expected_profit': expected_profit,
                             'profit_rank': profit_rank,
                             'month_label': month_label,
                             'profit_score': profit_rank * normalize_roi(roi)
                             }
            spreads.append(strike_spread)
    
    return {'symbol': symbol, 'spreads': sorted(spreads, key=lambda obj: obj['expected_profit'], reverse=True)}

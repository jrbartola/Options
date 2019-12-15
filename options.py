from tdameritrade import TDClient

from util import sort_by_strike

import os
import json

TOKEN = os.environ['TD_AMERITRADE_TOKEN']

c = TDClient(TOKEN)

def get_put_spreads():
    spreads = []
    option_data = c.options('HUBS', strategy='VERTICAL')['putExpDateMap']['2020-01-17:34']
    sorted_strikes = sort_by_strike(option_data)
    
    for i in range(len(sorted_strikes)-1):
        lower_strike, upper_strike = sorted_strikes[i:i+2]
        lower_strike, upper_strike = lower_strike[0], upper_strike[0]

        max_profit = upper_strike['bid'] - lower_strike['ask']
        max_loss = (upper_strike['strikePrice'] - lower_strike['strikePrice']) - max_profit
        strike_spread = {'strikes': '{}/{}'.format(lower_strike['strikePrice'], upper_strike['strikePrice']), 'max_profit': max_profit * 100, 'max_loss': max_loss * 100, 'roi': max_profit/max_loss}

        spreads.append(strike_spread)
    
    return sorted(spreads, key=lambda obj: obj['roi'], reverse=True)

print(json.dumps(get_put_spreads()))
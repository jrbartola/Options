from tdameritrade import TDClient
import numpy as np

from scipy.stats import norm

from util import compute_profit_rank

from functools import reduce
import os
import json

# This token has expired by now, so don't bother using it :)
TOKEN = 'goputIdAaoC2QKqlVaXyw6cShhM8ep+ghURJx72dDokBJAt/s9ljPq2sMIELSXhuUEytB86W/KtXkBrQMr0mhyo6bXF0dQkg6vY0LSMoTeIz6MaiJJDmgpWRd+k7p+GrakrPykQWEywGwNd0G4P5N/E32C2UYD+cxah9BkkrfkRXiyxBxfajoxqsVeCWW+H+4zbklD5LK06aX9+eFie16NZyCjiC6NlvQsJOx6tnPMzyvhsUBOxxxTnvAoUHtwDcs6ONHoZ/1Bo9NHp0GecUTfiSeuvp8ppKhkVx6Atu/biAnoq/5Rs6EVQd2Irmfdc8alMTTKWIFIMx27zxgkNKcImHgqN451uRYwmLdpupKeXF7BuoBWKpJWEr/0jWnZkLnfZ73l8+JGUt+DHuVuh0Pq7uBpSNDgrr3LKQH0yYXi7IWQvJ9VSB/f/J6euWMOlW5RXoIrIrkS4QNgF0n8MEsAGfLY5T7PJ+l8bmvQ/3GCuzs6xcW90hEBdnCHpP/ZKiv0IzPayaFxd7waT0DtHNma/LcFhyfI8rsJiPo100MQuG4LYrgoVi/JHHvlpCvUtr2Fpb8gwYfUekLS2Wnxz1X/NnQ35nXgq5jhbG5jEKqEKE0RcnNipcTJYKmv8V9CCNV4UhHA7gZtE2LGhikWkCMrN3/bBjkxXVfezNcfA07F456WLFaC/B3Ej/XXlA6V98uOg8O2rj+AyOxmhyo78k6lBnRsDxfqwTzNTuz+vQ83d+2jbKYBlSn6GmLzVL2vazX6LSgb4fsmw20L2PTanFNDPKmEThxNf4EcOGk74PWGGX0n6FMkece9aVn4J2/HenMH/wVQ2lBQU3i8L2SItJny2wApM0j1HyGj0WDrmmipzqCPPbehCkq2zGjp2lIm2ZPb7F9VADPUMtB6/IrC3sxeWBGQyIYd9n6wNZObLOxxBiauS34Sb1BFlclpVKOgVAMd/BGjM+n3iGGH8t9h/alNGmFOHlxAC8gFfAUJXqpT3Ceef1O/8LD1Z5PpY5hQ0WHMfqI90isWBKBII9s8YLWMTDyWDt/w+4RM6yHzeRGATSOmaymxvDHjd3l8QDLWjXkuRdUCkQ1bIcj5nUPYkLIkk0Y1dHBEl+212FD3x19z9sWBHDJACbC00B75E'

c = TDClient(TOKEN)

volatilities = {}
last_prices = {}

def calculate_daily_volatility(symbol):
    if symbol in volatilities:
        return volatilities[symbol]
    candles = c.history(symbol, periodType='year', period='1', frequencyType='daily')['candles']
    price_deltas = [candle['close']/candle['open'] - 1 for candle in candles]

    volatilities[symbol] = np.std(price_deltas)
    return volatilities[symbol]

def get_last_price(symbol):
    if symbol in last_prices:
        return last_prices[symbol]
    
    last_price = c.quote(symbol)[symbol]['lastPrice']
    last_prices[symbol] = last_price
    return last_price

def expected_profit(symbol, spread, high_strike, low_strike):
    daily_volatility = calculate_daily_volatility(symbol)
    last_price = get_last_price(symbol)

    RV = {'loc': last_price, 'scale': (32**0.5) * daily_volatility * last_price}

    p_below, p_above = norm.cdf(low_strike, **RV), (1 - norm.cdf(high_strike, **RV))
    p_between = 1 - p_above - p_below

    res = p_below * -spread['max_loss'] + p_between * (spread['max_profit'] - spread['max_loss']) + p_above * spread['max_profit']
    return res

def get_put_spreads(symbol):
    spreads = []
    strategy_data = c.options(symbol, strategy='VERTICAL', contractType='PUT')['monthlyStrategyList']
    
    for expiry_month in strategy_data:
        month_label = '{} {} {}'.format(expiry_month['month'], expiry_month['day'], expiry_month['year'])
        

        for strategy in filter(lambda strategy: strategy['strategyBid'] > 0, strategy_data):
            high_strike, low_strike = strategy['primaryLeg']['strikePrice'], strategy['secondaryLeg']['strikePrice']

            max_profit = (strategy['strategyBid'] + strategy['strategyAsk']) / 2
            max_loss = (high_strike - low_strike) - max_profit
            
            if max_loss == 0:
                continue

            strike_spread = {'strikes': strategy['strategyStrike'], 'max_profit': max_profit * 100, 'max_loss': max_loss * 100, 'roi': max_profit/max_loss}
            strike_spread['expected_profit'] = expected_profit(symbol, strike_spread, high_strike, low_strike)
            strike_spread['profit_rank'] = compute_profit_rank(strike_spread)
            spreads.append(strike_spread)
    
    return {'symbol': symbol, 'spreads': sorted(spreads, key=lambda obj: obj['profit_rank'], reverse=True)}

with open('test.json', 'w') as f:
    f.write(json.dumps(get_put_spreads('SPY')))

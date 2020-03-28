import numpy as np

from api.client import c


def get_price_quote(symbol):
    return c.quote(symbol)[symbol.upper()]

def get_historical_volatility(symbol):
    candles = c.history(symbol, periodType='year', period=1, frequencyType='daily')['candles']

    price_comps = [candles[i]['close'] / candles[i-1]['close'] - 1 for i in range(1, len(candles))]
    return np.std(price_comps) * (252**0.5)
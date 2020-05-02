import numpy as np

from options.api.client import get_client


def get_price_quote(symbol):
    return get_client().quote(symbol)[symbol.upper()]

def get_historical_volatility(symbol):
    candles = get_client().history(symbol, periodType='year', period=1, frequencyType='daily')['candles']

    price_comps = [candles[i]['close'] / candles[i-1]['close'] - 1 for i in range(1, len(candles))]
    return np.std(price_comps) * (252**0.5)
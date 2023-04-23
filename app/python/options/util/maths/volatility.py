import math


def to_dte_volatility(annual_volatility, dte):
    return annual_volatility * math.sqrt(dte / 365)

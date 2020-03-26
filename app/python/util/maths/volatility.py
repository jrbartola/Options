
def to_dte_volatility(annual_volatility, dte):
    daily_volatility = annual_volatility / (365**0.5)
    return daily_volatility * (dte ** 0.5)

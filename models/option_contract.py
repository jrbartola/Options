from scipy.stats import norm
from util import to_camel_case

class OptionContract(object):
    def __init__(self, price, symbol, contract_type, strike, dte, value, volatility):
        assert(contract_type in {'CALL', 'PUT'})

        self.underlying_price = price
        self.symbol = symbol[:symbol.index('_')]
        self.contract_type = contract_type
        self.strike = strike
        self.dte = dte
        self.value = value
        self.volatility = volatility
    
    def __repr__(self):
        return '<{symbol} {type} {strike} {dte}>'.format(symbol=self.symbol, type=self.contract_type, strike=self.strike, dte=self.dte)

    def prob_itm(self):
        # First, convert annual volatility to daily
        daily_volatility = self.volatility / (365**0.5)
        dte_volatility = daily_volatility * (self.dte ** 0.5)

        if self.contract_type == 'CALL':
            return 1 - norm.cdf(self.strike, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)

        return norm.cdf(self.strike, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)

    def prob_otm(self):
        return 1 - self.prob_itm()

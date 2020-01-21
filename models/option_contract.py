from scipy.stats import norm

from util import to_camel_case, to_dte_volatility


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
        return '<{symbol} {type} {strike} {dte} DTE>'.format(symbol=self.symbol, type=self.contract_type, strike=self.strike, dte=self.dte)
    
    @property
    def breakeven(self):
        if self.contract_type == 'CALL':
            return self.strike + abs(self.value)

        return self.strike - abs(self.value)

    def prob_itm(self):
        dte_volatility = to_dte_volatility(self.volatility, self.dte)

        if self.contract_type == 'CALL':
            return 1 - norm.cdf(self.strike, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)

        return norm.cdf(self.strike, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)

    def prob_otm(self):
        return 1 - self.prob_itm()

    def prob_profit(self):
        dte_volatility = to_dte_volatility(self.volatility, self.dte)
 
        # Short calls and long puts have the same profit profile
        if self.value > 0 and self.contract_type == 'CALL' or self.value < 0 and self.contract_type == 'PUT':
            return norm.cdf(self.breakeven, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)
        else:
            return 1 - norm.cdf(self.breakeven, loc=self.underlying_price, scale=self.underlying_price * dte_volatility)

from scipy.stats import norm

from models.spread import Spread
from util import to_dte_volatility

class VerticalSpread(Spread):
    def __init__(self, high_leg, low_leg):
        assert(high_leg.contract_type == low_leg.contract_type)
       
        self.contract_type = high_leg.contract_type
        self.high_leg = high_leg
        self.low_leg = low_leg
        self.dte = high_leg.dte

        # Credit if positive, debit if negative
        self.value = high_leg.value + low_leg.value

    def __repr__(self):
        return '<Vertical({} - {}) {}/{} [{} DTE]>'.format(self.high_leg.symbol, self.contract_type, self.low_leg.strike, self.high_leg.strike, self.dte)

    def __is_credit_spread(self):
        return self.value > 0

    @property
    def credit_percentage(self):
        if self.__is_credit_spread():
            return self.value / (self.high_leg.strike - self.low_leg.strike)

        return None
    
    @property
    def max_profit(self):
        if self.__is_credit_spread():
            return self.value

        return (self.high_leg.strike - self.low_leg.strike) + self.value
    
    @property
    def max_loss(self):
        if self.__is_credit_spread():
            return -(self.high_leg.strike - self.low_leg.strike) + self.value

        return self.value

    def expected_profit(self):
        avg_btw_strike_profit = self.max_profit - (self.high_leg.strike - self.low_leg.strike) / 2
        
        if self.contract_type == 'CALL':
            prob_in_the_middle = 1 - self.low_leg.prob_otm() - self.high_leg.prob_itm()
            if self.__is_credit_spread(): 
                return self.low_leg.prob_otm() * self.max_profit + self.high_leg.prob_itm() * self.max_loss + prob_in_the_middle * avg_btw_strike_profit
            
            return self.low_leg.prob_otm() * self.max_loss + self.high_leg.prob_itm() * self.max_profit + prob_in_the_middle * avg_btw_strike_profit
        
        if self.contract_type == 'PUT':
            prob_in_the_middle = 1 - self.low_leg.prob_itm() - self.high_leg.prob_otm()
            if self.__is_credit_spread():
                return self.low_leg.prob_itm() * self.max_loss + self.high_leg.prob_otm() * self.max_profit + prob_in_the_middle * avg_btw_strike_profit
            
            return self.low_leg.prob_itm() * self.max_profit + self.high_leg.prob_otm() * self.max_loss + prob_in_the_middle * avg_btw_strike_profit
        
        # Should never happen
        raise RuntimeError
    
    def prob_profit(self):
        dte_volatility = to_dte_volatility(self.low_leg.volatility, self.low_leg.dte)
        
        if self.__is_credit_spread():
            if self.contract_type == 'CALL':
                return norm.cdf(self.low_leg.strike + self.value, loc=self.low_leg.underlying_price, scale=self.low_leg.underlying_price * dte_volatility)
            
            return 1 - norm.cdf(self.high_leg.strike - self.value, loc=self.low_leg.underlying_price, scale=self.low_leg.underlying_price * dte_volatility)

    def has_fair_pricing(self):
        if self.__is_credit_spread():
            itm_prob = self.low_leg.prob_itm() if self.contract_type == 'CALL' else self.high_leg.prob_itm()
            return self.value > itm_prob * (self.high_leg.strike - self.low_leg.strike) 
        return False
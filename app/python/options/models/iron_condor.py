from options.models.spread import Spread

class IronCondor(Spread):
    def __init__(self, symbol, call_spread, put_spread, dte):
        self.symbol = symbol
        self.call_spread = call_spread
        self.put_spread = put_spread
        self.dte = dte
        self.credit = call_spread.max_profit + put_spread.max_profit

    def __repr__(self):
        return '<IronCondor({}) {}/{} - {}/{} [{} DTE] >'.format(self.symbol,
                                                                 self.put_spread.low_leg.strike,
                                                                 self.put_spread.high_leg.strike,
                                                                 self.call_spread.low_leg.strike,
                                                                 self.call_spread.high_leg.strike,
                                                                 self.dte)

    @property
    def credit_percentage(self):
        return self.credit / max(self.call_spread.high_leg.strike - self.call_spread.low_leg.strike,
                                 self.put_spread.high_leg.strike - self.put_spread.low_leg.strike)

    @property
    def max_profit(self):
        return self.credit

    @property
    def max_loss(self):
        return self.max_profit - max(self.call_spread.high_leg.strike - self.call_spread.low_leg.strike,
                                     self.put_spread.high_leg.strike - self.put_spread.low_leg.strike)

    def expected_profit(self):
        return self.call_spread.expected_profit() + self.put_spread.expected_profit()

    def prob_profit(self):
        return self.call_spread.prob_profit() + self.put_spread.prob_profit() - 1
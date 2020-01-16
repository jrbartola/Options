from models.spread import Spread

class IronCondor(Spread):
    def __init__(self, call_spread, put_spread, credit, dte):
        self.call_spread = call_spread
        self.put_spread = put_spread
        self.dte = dte

    @property
    def max_profit(self):
        return self.call_spread.max_profit + self.put_spread.max_profit

    @property
    def max_loss(self):
        return self.call_spread.max_loss + self.put_spread.max_loss

    def expected_profit(self):
        return self.call_spread.expected_profit() + self.put_spread.expected_profit()
from options.models.spread import Spread
from options.models.vertical_spread import VerticalSpread


class IronCondor(Spread):
    def __init__(
        self, symbol, call_spread: VerticalSpread, put_spread: VerticalSpread, dte
    ):
        self.symbol = symbol
        self.call_spread = call_spread
        self.put_spread = put_spread
        self.dte = dte
        self.credit = call_spread.max_profit + put_spread.max_profit

    def __repr__(self):
        return "{} IC {}/{}-{}/{} ({} DTE)".format(
            self.symbol,
            self.put_spread.low_leg.strike,
            self.put_spread.high_leg.strike,
            self.call_spread.low_leg.strike,
            self.call_spread.high_leg.strike,
            self.dte,
        )

    @property
    def credit_percentage(self):
        return abs(self.credit / self.max_loss)

    @property
    def max_profit(self):
        return self.credit

    @property
    def max_loss(self):
        return self.max_profit - max(
            self.call_spread.high_leg.strike - self.call_spread.low_leg.strike,
            self.put_spread.high_leg.strike - self.put_spread.low_leg.strike,
        )

    def expected_profit(self):
        return self.call_spread.expected_profit() + self.put_spread.expected_profit()

    def prob_profit(self):
        call_spread_prob_profit = self.call_spread.prob_profit()
        put_spread_prob_profit = self.put_spread.prob_profit()

        print(
            f"{self.__repr__()}: call sprad prob={call_spread_prob_profit}, call credit={self.call_spread.max_profit} put spread prop={put_spread_prob_profit} put credit={self.put_spread.max_profit}"
        )

        # Draw it out- it works
        return call_spread_prob_profit + put_spread_prob_profit - 1

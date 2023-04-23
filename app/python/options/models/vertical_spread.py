from scipy.stats import norm
import math

from options.constants.contracts import CALL, PUT
from options.models.spread import Spread
from options.models.option_contract import OptionContract
from options.util.maths.volatility import to_dte_volatility
from options.exceptions.invalid_spread import InvalidSpreadError


class VerticalSpread(Spread):
    def __init__(
        self, high_leg: OptionContract, low_leg: OptionContract, is_credit=False
    ):
        assert high_leg.contract_type == low_leg.contract_type

        self.contract_type = high_leg.contract_type
        self.high_leg = high_leg
        self.low_leg = low_leg
        self.dte = high_leg.dte
        self.is_credit = is_credit

        # TODO: Update support for debit spreads
        if self.contract_type == CALL:
            self.bid = self.low_leg.bid - self.high_leg.ask
            self.ask = self.low_leg.ask - self.high_leg.bid
        else:
            self.bid = self.high_leg.bid - self.low_leg.ask
            self.ask = self.high_leg.ask - self.low_leg.bid

        self.value = self.bid if self.is_credit else self.ask
        # self.value = (self.bid + self.ask) / 2

        if self.value < 0:
            raise InvalidSpreadError(
                f"Value of a vertical spread cannot be negative (got {self.value})"
            )

    def __repr__(self):
        return "<Vertical({} - {}) {}/{} [{} DTE]>".format(
            self.high_leg.symbol,
            self.contract_type,
            self.low_leg.strike,
            self.high_leg.strike,
            self.dte,
        )

    @property
    def credit_percentage(self):
        if self.is_credit:
            return self.value / (
                (self.high_leg.strike - self.low_leg.strike) - self.value
            )

        raise ValueError(
            "The method `credit_percentage` may only be called on a credit spread"
        )

    @property
    def max_profit(self):
        if self.is_credit:
            return self.value

        return (self.high_leg.strike - self.low_leg.strike) + self.value

    @property
    def max_loss(self):
        if self.is_credit:
            return -(self.high_leg.strike - self.low_leg.strike) + self.value

        return self.value

    def expected_profit(self):
        avg_btw_strike_profit = (
            self.max_profit - (self.high_leg.strike - self.low_leg.strike) / 2
        )

        if self.contract_type == CALL:
            prob_in_the_middle = 1 - self.low_leg.prob_otm() - self.high_leg.prob_itm()
            if self.is_credit:
                return (
                    self.low_leg.prob_otm() * self.max_profit
                    + self.high_leg.prob_itm() * self.max_loss
                    + prob_in_the_middle * avg_btw_strike_profit
                )

            return (
                self.low_leg.prob_otm() * self.max_loss
                + self.high_leg.prob_itm() * self.max_profit
                + prob_in_the_middle * avg_btw_strike_profit
            )

        else:
            prob_in_the_middle = 1 - self.low_leg.prob_itm() - self.high_leg.prob_otm()
            if self.is_credit:
                return (
                    self.low_leg.prob_itm() * self.max_loss
                    + self.high_leg.prob_otm() * self.max_profit
                    + prob_in_the_middle * avg_btw_strike_profit
                )

            return (
                self.low_leg.prob_itm() * self.max_profit
                + self.high_leg.prob_otm() * self.max_loss
                + prob_in_the_middle * avg_btw_strike_profit
            )

    def prob_profit(self):
        annual_volatility = (self.low_leg.volatility + self.high_leg.volatility) / 2
        dte_volatility = to_dte_volatility(annual_volatility, self.low_leg.dte)

        if self.is_credit:
            if self.contract_type == CALL:
                print(
                    f"Underlying={ self.low_leg.underlying_price}, target={self.low_leg.strike + self.value}, dte={self.low_leg.dte}, volatility={annual_volatility}"
                )
                z_score = (
                    math.log(
                        self.low_leg.underlying_price
                        / (self.low_leg.strike + self.value)
                    )
                    - 0.5 * (dte_volatility**2)
                ) / dte_volatility
                return 1 - norm.cdf(z_score)
            else:
                z_score = (
                    math.log(
                        self.low_leg.underlying_price
                        / (self.high_leg.strike - self.value)
                    )
                    - 0.5 * (dte_volatility**2)
                ) / dte_volatility
                return norm.cdf(z_score)

    def has_fair_pricing(self):
        if self.is_credit:
            itm_prob = (
                self.low_leg.prob_itm()
                if self.contract_type == CALL
                else self.high_leg.prob_itm()
            )
            return self.value > itm_prob * (self.high_leg.strike - self.low_leg.strike)

        raise ValueError(
            "The method `has_fair_pricing` may only be called on a credit spread"
        )

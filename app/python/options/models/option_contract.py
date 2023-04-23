from scipy.stats import norm
import math

from options.constants.contracts import CALL, PUT, CONTRACT_TYPES
from options.util.maths.volatility import to_dte_volatility


class OptionContract(object):
    def __init__(
        self, price, symbol, contract_type, strike, dte, bid, ask, is_short, volatility
    ):
        assert contract_type in CONTRACT_TYPES

        self.underlying_price = price
        self.symbol = symbol[: symbol.index("_")]
        self.contract_type = contract_type
        self.strike = strike
        self.dte = dte
        self.bid = bid
        self.ask = ask
        self.is_short = is_short
        self.volatility = volatility / 100

    def __repr__(self):
        return "<{symbol} {type} {strike} {dte} DTE>".format(
            symbol=self.symbol,
            type=self.contract_type,
            strike=self.strike,
            dte=self.dte,
        )

    @property
    def breakeven(self):
        if self.contract_type == CALL:
            if self.is_short:
                return self.strike + self.bid
            return self.strike + self.ask
        else:
            if self.is_short:
                return self.strike - self.bid
            return self.strike - self.ask

    def prob_itm(self) -> float:
        dte_volatility = to_dte_volatility(self.volatility, self.dte)

        z_score = (
            math.log(self.underlying_price / self.strike) + 0.5 * (dte_volatility**2)
        ) / dte_volatility

        if self.contract_type == CALL:
            return norm.cdf(z_score)

        return norm.cdf(-z_score)

    def prob_otm(self) -> float:
        return 1 - self.prob_itm()

    def prob_profit(self) -> float:
        dte_volatility = to_dte_volatility(self.volatility, self.dte)

        z_score = (
            math.log(self.underlying_price / self.breakeven)
            + 0.5 * (dte_volatility**2)
        ) / dte_volatility

        # Short calls and long puts have the same profit profile
        if (
            self.is_short
            and self.contract_type == CALL
            or not self.is_short
            and self.contract_type == PUT
        ):
            return norm.cdf(z_score)
        else:
            return 1 - norm.cdf(z_score)

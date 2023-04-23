from options.api.option_chain import get_option_chain
from options.api.quotes import get_price_quote

from options.constants.transactions import CREDIT, DEBIT
from options.constants.contracts import CALL, PUT
from options.models.option_contract import OptionContract
from options.models.vertical_spread import VerticalSpread
from options.util.maths.vix import vix
from options.exceptions.invalid_spread import InvalidSpreadError


def process_verticals(
    symbol, contract_type, credit_or_debit, max_strike_width=10, **kwargs
):
    assert credit_or_debit in {CREDIT, DEBIT}

    option_results = get_option_chain(symbol, **kwargs)

    if credit_or_debit == CREDIT:
        return process_credit_spreads(
            option_results["dte_maps"][contract_type],
            contract_type,
            option_results["price"],
            max_strike_width,
        )


def process_credit_spreads(
    dte_map, contract_type, underlying_price, max_strike_width=None
):
    result_dte_map = {}

    for dte, strike_map in dte_map.items():
        result_dte_map[dte] = {}
        sorted_strikes = sorted(strike_map.keys(), key=lambda strike: float(strike))

        for i in range(len(sorted_strikes) - 1):
            for j in range(i + 1, len(sorted_strikes)):
                low_strike = sorted_strikes[i]
                low_option = strike_map[low_strike]
                high_strike = sorted_strikes[j]
                high_option = strike_map[high_strike]

                if max_strike_width and high_strike - low_strike > max_strike_width:
                    break

                high_option_model = OptionContract(
                    price=underlying_price,
                    symbol=high_option["symbol"],
                    contract_type=contract_type,
                    strike=high_option["strikePrice"],
                    dte=dte,
                    bid=high_option["bid"],
                    ask=high_option["ask"],
                    is_short=contract_type == PUT,
                    volatility=high_option["volatility"],
                )

                low_option_model = OptionContract(
                    price=underlying_price,
                    symbol=low_option["symbol"],
                    contract_type=contract_type,
                    strike=low_option["strikePrice"],
                    dte=dte,
                    bid=low_option["bid"],
                    ask=low_option["ask"],
                    is_short=contract_type == CALL,
                    volatility=low_option["volatility"],
                )
                try:
                    vertical_model = VerticalSpread(
                        high_leg=high_option_model,
                        low_leg=low_option_model,
                        is_credit=True,
                    )
                except InvalidSpreadError as e:
                    print(f"{e}, skipping...")
                    continue

                strike_key = "{}/{}".format(
                    low_option_model.strike, high_option_model.strike
                )

                result_dte_map[dte][strike_key] = vertical_model

    return result_dte_map

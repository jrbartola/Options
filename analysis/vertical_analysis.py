
from option_chain import get_option_chain, get_price_quote, get_volatility

from models.option_contract import OptionContract
from models.vertical_spread import VerticalSpread

def analyze_verticals(symbol, contract_type, credit_or_debit, max_strike_width=50):
    assert(credit_or_debit in {'CREDIT', 'DEBIT'})

    dte_map = get_option_chain(symbol)[contract_type]
    stock_quote = get_price_quote(symbol)
    volatility = get_volatility(symbol)
    print('volatility is', volatility)

    if credit_or_debit == 'CREDIT':
        return analyze_credit_spreads(dte_map, contract_type, stock_quote, volatility, max_strike_width)

def analyze_credit_spreads(dte_map, contract_type, stock_quote, volatility, max_strike_width=None):
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

                high_option_model = OptionContract(price=stock_quote['lastPrice'],
                                                   symbol=high_option['symbol'],
                                                   contract_type=contract_type,
                                                   strike=high_option['strikePrice'],
                                                   dte=dte,
                                                   value=-high_option['ask'] if contract_type == 'CALL' else high_option['bid'],
                                                   volatility=volatility)

                low_option_model = OptionContract(price=stock_quote['lastPrice'],
                                                  symbol=low_option['symbol'],
                                                  contract_type=contract_type,
                                                  strike=low_option['strikePrice'],
                                                  dte=dte,
                                                  value=low_option['bid'] if contract_type == 'CALL' else -low_option['ask'],
                                                  volatility=volatility)

                vertical_model = VerticalSpread(high_leg=high_option_model, low_leg=low_option_model)
                strike_key = '{}/{}'.format(low_option_model.strike, high_option_model.strike)

                result_dte_map[dte][strike_key] = vertical_model
    
    return result_dte_map
                


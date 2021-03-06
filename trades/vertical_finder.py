import pandas as pd

from trades.filters.common_filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt
from processors.vertical_processors import process_verticals

from constants.transactions import CREDIT
from models.spread_filter import SpreadFilter
from models.option_contract import OptionContract

default_filter = SpreadFilter().add_criteria(lambda spread: spread.has_fair_pricing())

def find_verticals(symbol, contract_type, spread_filter=default_filter):
    data = process_verticals(symbol, contract_type, CREDIT, max_strike_width=10)
    spreads = []

    for dte in data:
        spreads.extend(data[dte].values())

    filtered_spreads = spread_filter.get_filtered(spreads)
    spread_data = [[spread.expected_profit() * 100, spread.credit_percentage, spread.prob_profit(), spread.max_profit, spread.max_loss] for spread in filtered_spreads]

    df = pd.DataFrame(data=spread_data, index=filtered_spreads, columns=['Expected Profit', 'Credit Percentage', 'Probability Profit', 'Max Profit', 'Max Loss'])
    
    return df.sort_values(by='Credit Percentage', ascending=False)

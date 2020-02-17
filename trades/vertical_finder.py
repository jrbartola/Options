import pandas as pd

from analysis.vertical_analysis import analyze_verticals
from models.option_contract import OptionContract
from analysis.filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt


def find_profitable_verticals(symbol, contract_type):
    data = analyze_verticals(symbol, contract_type, 'CREDIT', max_strike_width=10)
    spreads = []

    for dte in data:
        spreads.extend(data[dte].values())

    filtered_spreads = list(filter(lambda spread: spread.has_fair_pricing(), spreads))
    spread_data = [[spread.expected_profit() * 100, spread.credit_percentage, spread.prob_profit(), spread.max_profit, spread.max_loss] for spread in filtered_spreads]

    df = pd.DataFrame(data=spread_data, index=filtered_spreads, columns=['Expected Profit', 'Credit Percentage', 'Probability Profit', 'Max Profit', 'Max Loss'])
    
    print(df.sort_values(by='Credit Percentage', ascending=False))

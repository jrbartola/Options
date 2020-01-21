import numpy as np
import pandas as pd

from analysis.vertical_analysis import analyze_verticals
from models.option_contract import OptionContract
from analysis.filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt


def main():
    data = analyze_verticals('SPY', 'CALL', 'CREDIT', max_strike_width=10)
    thirty_days = data[30]

    spreads = sorted([thirty_days[strkey] for strkey in thirty_days.keys()], key=lambda x: x.expected_profit(), reverse=True)
    filtered_spreads = list(filter(lambda spread: credit_percentage_gt(0.3)(spread) and prob_profit_gt(0.5)(spread) and expected_profit_gt(0.0)(spread), spreads))
    
    spread_data = [[spread.expected_profit() * 100, spread.credit_percentage, spread.prob_profit()] for spread in filtered_spreads]

    df = pd.DataFrame(data=spread_data, index=filtered_spreads, columns=['Expected Profit', 'Credit Percentage', 'Probability Profit'])
    
    print(df.sort_values(by='Credit Percentage', ascending=False))
    return filtered_spreads

if __name__ == '__main__':
    # low_leg = OptionContract(331.95, 'SPY_', 'CALL', 320, 32, 13.69, 0.1183)
    # high_leg = OptionContract(331.95, 'SPY_', 'CALL', 325, 32, -9.31, 0.1183)

    # print(low_leg.prob_itm(), high_leg.prob_itm())
    main()
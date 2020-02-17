import pandas as pd

from processors.filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt, max_profit_gt
from processors.vertical_processors import process_verticals

from constants.transactions import CREDIT
from constants.contracts import CALL, PUT
from models.iron_condor import IronCondor


def find_profitable_iron_condors(symbol, prob_profit=0.5):
    call_data = process_verticals(symbol, CALL, CREDIT, max_strike_width=10)
    put_data = process_verticals(symbol, PUT, CREDIT, max_strike_width=10)
    call_spreads = []
    put_spreads = []
    iron_condors = []

    for dte in call_data:
        call_spreads.extend(call_data[dte].values())
        put_spreads.extend(put_data[dte].values())

    for i in range(len(call_spreads)):
        for j in range(len(put_spreads)):
            call_spread = call_spreads[i]
            put_spread =  put_spreads[j]
            
            # No inversions allowed
            if call_spread.low_leg.strike < put_spread.high_leg.strike:
                break

            iron_condors.append(IronCondor(symbol, call_spread, put_spread, dte=call_spread.dte))

    filtered_spreads = list(filter(lambda spread: credit_percentage_gt(0.3)(spread) and prob_profit_gt(prob_profit)(spread) and expected_profit_gt(0.0)(spread), iron_condors))
    spread_data = [[spread.expected_profit() * 100, spread.credit_percentage, spread.prob_profit(), spread.max_profit, spread.max_loss] for spread in filtered_spreads]

    df = pd.DataFrame(data=spread_data, index=filtered_spreads, columns=['Expected Profit', 'Credit Percentage', 'Probability Profit', 'Max Profit', 'Max Loss'])
    
    print(df.sort_values(by='Credit Percentage', ascending=False))

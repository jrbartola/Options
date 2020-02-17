import pandas as pd

from analysis.vertical_analysis import analyze_verticals
from models.iron_condor import IronCondor
from analysis.filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt, max_profit_gt


def find_profitable_iron_condors(symbol, prob_profit=0.5):
    call_data = analyze_verticals(symbol, 'CALL', 'CREDIT', max_strike_width=10)
    put_data = analyze_verticals(symbol, 'PUT', 'CREDIT', max_strike_width=10)
    call_spreads = []
    put_spreads = []
    iron_condors = []

    for dte in call_data:
        call_spreads.extend(call_data[dte].values())
        put_spreads.extend(put_data[dte].values())

    for i in range(len(call_spreads) - 1):
        for j in range(i + 1, len(call_spreads)):
            call_spread = call_spreads[i]
            put_spread =  put_spreads[j]
            if call_spread.value > 0 and put_spread.value > 0:
                iron_condors.append(IronCondor(symbol, call_spread, put_spread, dte=call_spreads[i].dte))

    # filtered_spreads = list(filter(lambda spread: credit_percentage_gt(0.3)(spread) and prob_profit_gt(prob_profit)(spread) and expected_profit_gt(0.0)(spread), iron_condors))
    spread_data = [[spread.expected_profit() * 100, spread.credit_percentage, spread.prob_profit(), spread.max_profit, spread.max_loss] for spread in iron_condors]

    # df = pd.DataFrame(data=spread_data, index=filtered_spreads, columns=['Expected Profit', 'Credit Percentage', 'Probability Profit', 'Max Profit', 'Max Loss'])
    
    print(df.sort_values(by='Credit Percentage', ascending=False))

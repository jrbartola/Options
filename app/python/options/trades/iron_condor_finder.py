import pandas as pd
from functools import reduce

from options.trades.filters.common_filters import prob_profit_gt, expected_profit_gt, credit_percentage_gt
from options.processors.vertical_processors import process_verticals

from options.constants.transactions import CREDIT
from options.constants.contracts import CALL, PUT
from options.models.spread_filter import SpreadFilter
from options.models.iron_condor import IronCondor

def find_iron_condors(symbol, spread_filters=[], **kwargs):
    call_data = process_verticals(symbol, CALL, CREDIT, **kwargs)
    put_data = process_verticals(symbol, PUT, CREDIT, **kwargs)
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

    filtered_spreads = reduce(lambda spreads, spread_filter: [spread for spread in spreads if spread_filter.filter(spread)], spread_filters, iron_condors)
    spread_data = [[spread.expected_profit(), spread.credit_percentage, spread.prob_profit(), spread.max_profit, spread.max_loss] for spread in filtered_spreads]

    df = pd.DataFrame(data=spread_data, index=[repr(s) for s in filtered_spreads], columns=['expectedProfit', 'creditPercent', 'probProfit', 'maxProfit', 'maxLoss'])
    
    return df.sort_values(by='creditPercent', ascending=False)

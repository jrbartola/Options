# Preprocesses some data to set up for VIX calculations: http://www.cboe.com/micro/vix/vixwhite.pdf

from constants.contracts import CALL, PUT

def combine_contract_data(calls, puts):
    # Sanity check - DTE should be identical for calls and puts
    assert(calls.keys() == puts.keys())

    dte_map = {}

    for dte in calls.keys():
        dte_map[dte] = {}

        call_strikemap, put_strikemap = calls[dte], puts[dte]
        
        assert(call_strikemap.keys() == put_strikemap.keys())
        for strike in call_strikemap:
            dte_map[dte][strike] = {CALL: call_strikemap[strike],
                                    PUT: put_strikemap[strike]}
    
    return dte_map

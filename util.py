
def map_to(l, f):
    return [f(item) for item in l]

def map_to_str(l):
    return map_to(l, str)

def map_to_float(l):
    return map_to(l, float)

def sort_by_strike(strike_dict):
    sorted_strikes = map_to_str(sorted(map_to_float(strike_dict.keys())))
    
    return [strike_dict[price] for price in sorted_strikes]

def compute_profit_rank(expected_profit, max_profit):
    if expected_profit < 0:
        return 0
    return expected_profit / max_profit

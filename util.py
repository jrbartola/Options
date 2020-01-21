
def map_to(l, f):
    return [f(item) for item in l]

def map_to_str(l):
    return map_to(l, str)

def map_to_float(l):
    return map_to(l, float)

def to_camel_case(str): 
    return ''.join(['_'+i.lower() if i.isupper() else i for i in str]).lstrip('_') 

def to_dte_volatility(annual_volatility, dte):
    daily_volatility = annual_volatility / (365**0.5)
    return daily_volatility * (dte ** 0.5)

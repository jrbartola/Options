
def map_option_chain(expiration_map, filter_fn=lambda _: True):
    result = {}

    for expir_str, strike_map in expiration_map.items():
        dte = int(expir_str[expir_str.index(':') + 1 :])
        result[dte] = {}
        
        for strike_str, option_arr in strike_map.items():
            option = option_arr[0] # TODO: Will this ever throw an error?

            if filter_fn(option):
                result[dte][float(strike_str)] = option
    
    return result
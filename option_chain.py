from tdameritrade import TDClient
import numpy as np

from mappers import map_option_chain

from datetime import datetime, timedelta

# This token has expired by now, so don't bother using it :)
TOKEN = '+4A1xIQKx5E+HenzTLQFjGPiSGFfAl/TZXIXN8k2QYoeHYqn1h8F1CCnxKPOMKBHcboQA6rzwIHN8s8+GJZH6m90aBFwufbwwF3V3PR3JxAF6HiXWVzGPB+JvlhZujL43OgwwuPdX8hVbRE9xhYGNmHsCECxRCzWmsUO/QhWCrXRjGNqzcHWZBrt+aNDPdLibdYyjRXJCe3UVi1YKP/LBnYNbHRln0fxTiDdd+YgN4gWssQiSAa/pU+ySy89A019Y6Jt4SV7RyzRXcvOU7r1G3XQpG826hbIQpX4G+vGQ1k+BYW3qLpjFOwzJPrQO6f1Mom6NApLOPZodYbEGHurOP5eFrihlLILLoLf5tRci/93Jlt3shKtGfR8IuEn+91iqvLI0mp1bZ6WFR3lcShPGFnsEKa9tOnUpGmI96dOSTRHNUVf/AnSMb1Zlaqc9Y33tfr4n9k4Wvc5P4QtXzIg/fXhHKncWw2Lz6zUuvmoF1ks34H4xY+ZyFIL7rJkYOjweTMDEWDFtO/E8qBcN39LjHvaPOfGfKNTT+Teu2Va/NIeyBhcV100MQuG4LYrgoVi/JHHvlHJGAWDwGtlD0cgZkUqDhO/WGhO9E8DTrAo1ADrCI1t0ioj7z951KajQE3DYGLgDsCxKHr9LQzWfhiMACU5RooaN9YXju4cNEByANrJJOEINO4G/+b+0Q80p51kNAnle0huUJMkVXeQtGXavJOgNOqL2wIe0B375Zksx+GJCeZxYfzjDbZ+Nv3L0o9O0jeZli98nIrOqpFJt1dDZgWC/OO4XDjczBArjfzdBNVK/VRwRVg1qkkeupyFcgihV7V1Ry2gCwMYXoNpS7tcuvjYMpbP/rhFgwQ52F4Mix1KmXJalgimvGmKi2j4NmNfybpBtFMYbJbOvBCoQAoOfK8Qg04HSXBPW+xBb+vWXntH9aeuKnZGo6MM0+Vw9HIoF/9itrYQGAc+fgtILd77YbVN3CCjaWT8cqZ02cVCjyuUVgwxoSo3KnfnkGN0th7doXN89tZ2rNxDesY+/48K5vOSgFY2akawm8/vCNF3y4UprU8iz52MC9ypMklZ+IanjF85aKqszPHkEqLhO6fRxXYRN0+xvRSor40Gll+VSGb75L924rL/jQ==212FD3x19z9sWBHDJACbC00B75E'

c = TDClient(TOKEN)

def get_option_chain(symbol, low_dte=30, high_dte=45, min_volume=50):
    from_date = (datetime.now() + timedelta(days=low_dte)).isoformat()
    to_date = (datetime.now() + timedelta(days=high_dte)).isoformat()

    data = c.options(symbol, strategy='ANALYTICAL', fromDate=from_date, toDate=to_date, optionType='S')
    call_data = data['callExpDateMap']
    put_data = data['putExpDateMap']

    volume_filter = lambda option: option['totalVolume'] < min_volume

    return {'CALL': map_option_chain(call_data, volume_filter), 'PUT': map_option_chain(put_data, volume_filter)}

def get_price_quote(symbol):
    return c.quote(symbol)[symbol.upper()]

def get_volatility(symbol):
    candles = c.history(symbol, periodType='year', period=1, frequencyType='daily')['candles']

    price_diffs = [candle['close'] / candle['open'] - 1 for candle in candles]
    return np.std(price_diffs)
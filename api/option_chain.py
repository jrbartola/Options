import numpy as np
from datetime import datetime, timedelta

from util.mappers import map_option_chain
from api.client import c

def get_option_chain(symbol, low_dte=30, high_dte=45, min_volume=50):
    from_date = (datetime.now() + timedelta(days=low_dte)).isoformat()
    to_date = (datetime.now() + timedelta(days=high_dte)).isoformat()

    data = c.options(symbol, strategy='ANALYTICAL', fromDate=from_date, toDate=to_date, optionType='S')
    if 'error' in data:
        raise ValueError(f'''Error occured while fetching option chain: {data['error']}''')

    call_data = data['callExpDateMap']
    put_data = data['putExpDateMap']

    volume_filter = lambda option: option['totalVolume'] > min_volume

    return {'CALL': map_option_chain(call_data, volume_filter), 'PUT': map_option_chain(put_data, volume_filter)}, data['underlyingPrice']

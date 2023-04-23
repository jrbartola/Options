import numpy as np
from datetime import datetime, timedelta

from options.constants.contracts import CALL, PUT
from options.util.mappers import map_option_chain
from options.api.client import get_client


def get_option_chain(symbol, low_dte=30, high_dte=45, min_volume=50, **kwargs):
    from_date = (datetime.now() + timedelta(days=low_dte)).isoformat()
    to_date = (datetime.now() + timedelta(days=high_dte)).isoformat()

    data = get_client().options(
        symbol,
        strategy="ANALYTICAL",
        fromDate=from_date,
        toDate=to_date,
        range="OTM",
        optionType="S",
    )
    if "error" in data:
        raise ValueError(
            f"""Error occured while fetching option chain: {data['error']}"""
        )

    call_data = data["callExpDateMap"]
    put_data = data["putExpDateMap"]

    volume_filter = lambda option: option["totalVolume"] >= min_volume

    return {
        "dte_maps": {
            CALL: map_option_chain(call_data, volume_filter),
            PUT: map_option_chain(put_data, volume_filter),
        },
        "price": data["underlyingPrice"],
    }

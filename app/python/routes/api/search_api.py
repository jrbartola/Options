from flask import Blueprint, render_template, request, jsonify, abort

from routes.api.exceptions.bad_request import BadRequest
from options.trades.iron_condor_finder import find_iron_condors
from options.constants.strategies import IRON_CONDOR, CREDIT_VERTICAL
from options.models.spread_filter import SpreadFilter

search_api = Blueprint('search_api', __name__, url_prefix='/api/v1')

@search_api.route("/search/strategy/<strategy_type>", methods=["POST"])
def search_strategy(strategy_type):

    symbol = request.args.get('symbol')
    filters = request.json.get('filters')
    low_dte = request.json.get('low_dte')
    high_dte = request.json.get('high_dte')
    volatility = request.json.get('volatility')

    if strategy_type not in [IRON_CONDOR, CREDIT_VERTICAL]:
        raise BadRequest(f'Invalid strategy `{strategy_type}`, expected one of [{IRON_CONDOR}, {CREDIT_VERTICAL}]')

    if symbol is None:
        raise BadRequest('Missing expected query parameter `symbol`', missing_value='symbol')

    if filters is None:
        raise BadRequest('Missing expected body parameter `filters`', missing_value='filters')

    
    spread_filters = [SpreadFilter(filter.filter_type, filter.comparison_op, filter.filter_value) for filter in filters] 

    results = find_iron_condors(symbol, symbol=symbol, spread_filters=spread_filters, low_dte=low_dte, high_dte=high_dte, volatility=volatility)

    return jsonify(results)

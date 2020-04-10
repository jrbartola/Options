from flask import Blueprint, render_template, request, jsonify, abort

from routes.api.exceptions.bad_request import BadRequest
from options.trades.iron_condor_finder import find_iron_condors
from options.constants.strategies import IRON_CONDOR, CREDIT_VERTICAL
from options.trades.filters

search_api = Blueprint('search_api', __name__, url_prefix='/api/v1')

@search_api.route("/search/strategy/<strategy_type>", methods=["POST"])
def search_strategy(strategy_type):

    symbol = request.args.get('symbol')
    filters = request.json.get('filters')
    dte = request.json.get('dte')
    volatility = request.json.get('volatility')

    if strategy_type not in [IRON_CONDOR, CREDIT_VERTICAL]:
        raise BadRequest(f'Invalid strategy `{strategy_type}`, expected one of [{IRON_CONDOR}, {CREDIT_VERTICAL}]')

    if symbol is None:
        raise BadRequest('Missing expected query parameter `symbol`', missing_value='symbol')

    if filters is None:
        raise BadRequest('Missing expected body parameter `filters`', missing_value='filters')
    
    if dte is None:
        raise BadRequest('Missing expected body parameter `dte`', missing_value='dte')

    spread_filter = SpreadFilter().add_criteria(credit_percentage_gt(0.3)) \
                               .add_criteria(prob_profit_gt(0.5)) \
                               .add_criteria(expected_profit_gt(0.0))



    results = find_iron_condors(symbol, symbol=symbol, dte=dte, spread_filter=spread_filter, volatility=volatility, )

    return jsonify(results)

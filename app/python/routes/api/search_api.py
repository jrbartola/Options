from flask import Blueprint, render_template, request, jsonify, abort, make_response
from werkzeug.exceptions import HTTPException
import traceback
import json

from routes.api.exceptions.bad_request import BadRequest
from options.trades.iron_condor_finder import find_iron_condors
from options.constants.strategies import IRON_CONDOR, CREDIT_VERTICAL
from options.models.spread_filter import SpreadFilter

search_api = Blueprint('search_api', __name__, url_prefix='/api/v1')

@search_api.route("/search/strategy/<strategy_type>", methods=["POST"])
def search_strategy(strategy_type):

    symbol = request.args.get('symbol')
    filters = request.json.get('filters')
    low_dte = request.json.get('lowDte')
    high_dte = request.json.get('highDte')
    volatility = request.json.get('volatility')

    if strategy_type not in [IRON_CONDOR, CREDIT_VERTICAL]:
        raise BadRequest(f'Invalid strategy `{strategy_type}`, expected one of [{IRON_CONDOR}, {CREDIT_VERTICAL}]')

    if symbol is None:
        raise BadRequest('Missing expected query parameter `symbol`', missing_value='symbol')

    if filters is None:
        raise BadRequest('Missing expected body parameter `filters`', missing_value='filters')

    
    spread_filters = [SpreadFilter(filter['filterType'], filter['comparisonOp'], filter['filterValue']) for filter in filters] 

    results = find_iron_condors(symbol, spread_filters=spread_filters, low_dte=low_dte, high_dte=high_dte, volatility=volatility)

    # Parse results
    merged = {'results': json.loads(results.to_json(orient='index')), 'strategyType': strategy_type}
    return jsonify(merged)


# 400 handler
@search_api.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# 500+ errors/generic catchall
@search_api.errorhandler(Exception)
def handle_server_error(e):
    error = {
        "message": str(e),
        "trace": traceback.format_exc()
    }
    return make_response(jsonify(error), 500)

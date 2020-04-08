from flask import Blueprint, render_template, request, jsonify, abort

from options.trades.iron_condor_finder import find_iron_condors

search_api = Blueprint('search_api', __name__, url_prefix='/api/v1')

@search_api.route("/search/strategy/<strategy_type>", methods=["POST"])
def search_strategy(alias):

    try:
        symbol = request.json['symbol']
        results = find_iron_condors(symbol)

        return jsonify(results)
    except KeyError:
        
    except Exception:

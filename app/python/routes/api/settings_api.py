from flask import Blueprint, request, jsonify
import os

from routes.api.exceptions.bad_request import BadRequest

settings_api = Blueprint('settings_api', __name__, url_prefix='/api/v1')

@settings_api.route("/settings", methods=["POST"])
def update_settings():
    key = request.json.get('key')
    value = request.json.get('value')
    
    if key is None:
        raise BadRequest('Missing expected body parameter `key`', missing_value='key')

    if value is None:
        raise BadRequest('Missing expected body parameter `value`', missing_value='value')
    
    try:
        os.environ[key] = value
        assert(os.environ[key] == value)

        return '', 204
    except Exception as e:
        return jsonify({'message': str(e)}), 500
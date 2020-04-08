from flask import Blueprint, render_template, jsonify

from routes.api.exceptions.bad_request import BadRequest

main_views = Blueprint('main_routes', __name__)

@main_views.route('/')
def main(**kwargs):
    return render_template("index.html")

# Error handlers

@main_views.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
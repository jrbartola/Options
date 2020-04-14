from flask import Blueprint, render_template, jsonify
from werkzeug.exceptions import HTTPException
import json

from routes.api.exceptions.bad_request import BadRequest

main_views = Blueprint('main_routes', __name__)

@main_views.route('/')
def main(**kwargs):
    return render_template("index.html")

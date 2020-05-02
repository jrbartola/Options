from flask import Flask

from log import add_logger
from config import configure_app
from db.connection import db
from db.marshmallow import ma
from routes.views import main_views
from routes.api.search_api import search_api
from routes.api.settings_api import settings_api

def create_flask_app():
    app = Flask(__name__, static_folder="../www/static", template_folder="../www/static/templates")
    configure_app(app)

    db.init_app(app)
    ma.init_app(app)
    
    register_blueprints(app, [main_views, search_api, settings_api])
    
    add_logger(app)
    
    return app

def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
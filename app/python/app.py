from flask import Flask

from log import add_logger
from config import configure_app
from db.connection import db
from db.marshmallow import ma
from routes.views import main_views

def create_flask_app():
    app = Flask(__name__, static_folder="../www/static", template_folder="../www/static/templates")
    configure_app(app)

    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(main_views)
    
    add_logger(app)
    
    return app


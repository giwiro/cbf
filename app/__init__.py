import os
from flask import Flask
from app.db import mongo, init_db
from app.splash import splash_module
from app.search import search_module
from app.feedback import feedback_module

def set_up_routes(app):
    app.register_blueprint(splash_module)
    app.register_blueprint(search_module)
    app.register_blueprint(feedback_module)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_pyfile("config.py")

    mongo_uri = os.environ.get('MONGO_URI') or "mongodb://localhost/cbf"
    app.config["MONGO_URI"] = mongo_uri

    init_db(app)
    set_up_routes(app)
    return app

from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    print("DB Initialized")
    mongo.init_app(app)


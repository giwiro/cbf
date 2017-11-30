from flask import Blueprint, render_template
from app.db import mongo

splash_module = Blueprint("splash", __name__)

@splash_module.route("/")
def show_splash():
    books = mongo.db.books.find()
    return render_template("index2.html", books=books)



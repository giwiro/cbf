from flask import Blueprint, render_template, request
from app.db import mongo

import pprint

feedback_module = Blueprint("feedback", __name__)

@feedback_module.route("/feedback", methods=["POST"])
def positive():
    feedback_type = request.form["feedback_type"]
    request_book = request.form["request_book"]
    result_book_ids = list(map(lambda x: int(x), request.form.getlist('result_book_ids[]')))
    f = {"request_book": request_book, "type": feedback_type, "result_books": result_book_ids}
    mongo.db.feedback.insert(f)
    return render_template("thanks.html")


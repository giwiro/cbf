from flask import Blueprint, render_template, request
from app.db import mongo

search_module = Blueprint("search", __name__)

@search_module.route("/search", methods=["POST"])
def search():
    id = int(request.form["book_id"])
    query = {"$or": [{ "bookA": id }, { "boolB": id }]}
    result = mongo.db.relations.find(query)
    book_ids = [int(r["bookA"]) if r["bookA"] != id else r["bookB"] for r in result]
    result_query = {"id": {"$in": book_ids}}
    books = mongo.db.books.find(result_query).sort([("value", -1)]).limit(10)
    request_book = mongo.db.books.find_one({"id": id})
    return render_template("result.html",
            request_book=request_book, book_ids=book_ids, books=books,)


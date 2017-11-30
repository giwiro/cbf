from flask import Blueprint, render_template, request
from app.db import mongo

import pprint
search_module = Blueprint("search", __name__)

@search_module.route("/search", methods=["POST"])
def search():
    id = int(request.form["book_id"])
    query = {"$or": [{ "bookA": id }, { "boolB": id }]}
    result = mongo.db.relations.find(query)
    book_ids = []
    books_value = {}
    for r in result:
        key = int(r["bookA"]) if r["bookA"] != id else int(r["bookB"])
        book_ids.append(key)
        content = dict({"value": r["value"]})
        books_value[key] = content

    # pprint.pprint(books_value)
    result_query = {"id": {"$in": book_ids}}
    books_result = mongo.db.books.find(result_query).sort([("value", -1)]).limit(10)
    for br in books_result:
        books_value[int(br["id"])].update(br)
    

    # pprint.pprint(books_value)
    request_book = mongo.db.books.find_one({"id": id})
    return render_template("result.html",
            request_book=request_book, book_ids=book_ids, books=list(books_value.values()),)


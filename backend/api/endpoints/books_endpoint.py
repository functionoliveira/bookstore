from app import app
from flask import request
from controllers import BooksController

@app.route("/books/", methods=['POST'])
def endpoint_create_books():
    controller = BooksController(request)
    return controller.create()

@app.route("/books/", methods=['GET'])
def endpoint_list_books():
    controller = BooksController(request)
    return controller.list_books()

@app.route("/books/<id>/")
def endpoint_get_books(id=None):
    controller = BooksController(request)
    return controller.get_books_by_Id(id)
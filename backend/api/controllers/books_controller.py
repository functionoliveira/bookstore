from flask import jsonify
from .controller import Controller
from services import BooksService

class BooksController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)

    def create(self):
        service = BooksService()
        return service.create(self.body)

    def list_books(self, filter=None):
        service = BooksService()
        return jsonify(service.list())
    
    def get_books_by_Id(self, id):
        service = BooksService()
        return service.get_by_id(id)

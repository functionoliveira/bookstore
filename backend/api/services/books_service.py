from models import Books
from app import db
from factories import create_books
from flask import abort

class BooksService:
    def create(self, data):
        title = data['title']
        author = data['author']
        unit_price = data['unit_price']
        books = Books(title, author, unit_price)
        db.session.add(books)
        db.session.commit()
        return create_books(books)

    def list(self):
        list_of_books = Books.query.order_by(Books.title).all()
        return [create_books(book) for book in list_of_books]
    
    def get_by_id(self, id):
        book = Books.query.filter_by(id=id).first()
        if book is None:
            abort(404, description="Books not found")
        return create_books(book)
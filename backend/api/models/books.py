from app import db

class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    unit_price = db.Column(db.Float())

    def __init__(self, title, author, unit_price):
        self.title = title
        self.author = author
        self.unit_price = unit_price

    def __repr__(self):
        return '<id {}>'.format(self.id)
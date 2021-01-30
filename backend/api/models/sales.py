from app import db

class Sales(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    total = db.Column(db.Float())
    discount = db.Column(db.Integer())
    items = db.relationship("Items")

    def __init__(self, customer_id, total, discount):
        self.customer_id = customer_id
        self.total = total
        self.discount = discount
        self.items = []

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Items(db.Model):
    __tablename__ = 'items'
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id'), primary_key=True)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    def __init__(self, sales_id, books_id, quantity):
        self.sales_id = sales_id
        self.books_id = books_id
        self.quantity = quantity
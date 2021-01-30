from app import db

class Customers(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String())
    email = db.Column(db.String())
    documentType = db.Column(db.String())
    documentNumber = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(self, fullName, email, documentType, documentNumber, address):
        self.fullName = fullName
        self.email = email
        self.documentType = documentType
        self.documentNumber = documentNumber
        self.address = address

    def __repr__(self):
        return '<id {}>'.format(self.fullName)

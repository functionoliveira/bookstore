from models import Customers
from app import db
from factories import create_customers
from flask import abort

class CustomersService:
    def create(self, data):
        full_name = data['full_name']
        email = data['email']
        document_type = data['document_type']
        document_number = data['document_number']
        address = data['address']
        customers = Customers(full_name, email, document_type, document_number, address)
        db.session.add(customers)
        db.session.commit()
        return create_customers(customers)

    def list(self):
        list_of_customers = Customers.query.order_by(Customers.fullName).all()
        return [create_customers(customers) for customers in list_of_customers]
    
    def get_by_id(self, id):
        customers = Customers.query.filter_by(id=id).first()
        if customers is None:
            abort(404, description="Customers not found")
        return create_customers(customers)
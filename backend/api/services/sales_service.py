from models import Sales, Items, Books
from app import db
from factories import create_sales
from services import BooksService
from flask import abort

class SalesService:
    def create(self, data):
        customers_id = data['customers_id']
        items = data['items']
        self.buy_at_most_ten_diferrent_books(items)
        price = self.apply_discount(items, customers_id)
        total = price.total
        discount = price.discount

        sales = Sales(customers_id, total, discount)
        db.session.add(sales)

        for item in items:
            new_items = Items(sales.id, item['books_id'], item['quantity'])
            sales.items.append(new_items)
            db.session.add(new_items)
        db.session.commit()

        return create_sales(sales)

    def list(self):
        list_of_sales = Sales.query.all()
        return [create_sales(sales) for sales in list_of_sales]
    
    def get_by_id(self, id):
        sales = Sales.query.filter_by(id=id).first()
        if sales is None:
            abort(404, description="Sales not found")
        return create_sales(sales)
    
    def find_total(self,items):
        total = 0
        books_service = BooksService()

        for item in items:
            books_price = books_service.get_by_id(item['books_id'])['unit_price']
            total += books_price * item['quantity']
        
        return total

    def apply_discount(self, items, customer_id):
        total = self.find_total(items)
        discount = self.has_discount(customer_id)
        percent_discount = (1 - (discount / 100))
        return Price(round(total * percent_discount, 2), discount)
    
    # Caso não haja desconto o valor retornado é zero
    def has_discount(self, customer_id):
        total = 0
        sales_by_customer = Sales.query.filter_by(customer_id=customer_id).all()

        for sales in sales_by_customer:
            total += sales.total

        if total < 1000:
            return 0
        elif total < 5001:
            return 10
        elif total < 15001:
            return 15
        else:
            return 20

    def buy_at_most_ten_diferrent_books(self, items):
        if len(items) > 10:
            abort(500, description="The customer can buy at most 10 different books on the same sale")

class Price:
    def __init__(self, total, discount):
        self.total = total
        self.discount = discount
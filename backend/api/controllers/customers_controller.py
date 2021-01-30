from flask import jsonify
from .controller import Controller
from services import CustomersService

class CustomersController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)

    def create_customers(self):
        service = CustomersService()
        return service.create(self.body)
    
    def list_customers(self):
        service = CustomersService()
        return jsonify(service.list())
    
    def get_customers_by_Id(self, id):
        service = CustomersService()
        return service.get_by_id(id)
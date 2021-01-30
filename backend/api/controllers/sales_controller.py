from flask import jsonify
from .controller import Controller
from services import SalesService

class SalesController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)

    def create_sales(self):
        # try:
        service = SalesService()
        return service.create(self.body)
        # except Exception as e:
        #     return { "code": "#SALES0001", "title": "Create Sales", "description": "erro ao tentar cadastrar venda." }
    
    def list_sales(self):
        service = SalesService()
        return jsonify(service.list())
    
    def get_sales_by_Id(self, id):
        service = SalesService()
        return service.get_by_id(id)
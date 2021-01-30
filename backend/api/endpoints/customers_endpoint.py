from app import app
from flask import request
from controllers import CustomersController

@app.route("/customers/", methods=['POST'])
def endpoint_create_customers():
    controller = CustomersController(request)
    return controller.create_customers()

@app.route("/customers/", methods=['GET'])
def endpoint_get_customers():
    controller = CustomersController(request)
    return controller.list_customers()

@app.route("/customers/<id>/")
def endpoint_get_customers_by_id(id=None):
    controller = CustomersController(request)
    return controller.get_customers_by_Id(id)
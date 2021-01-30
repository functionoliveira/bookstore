from app import app
from flask import request
from controllers import SalesController

@app.route("/sales/", methods=['POST'])
def endpoint_create_sales():
    controller = SalesController(request)
    return controller.create_sales()

@app.route("/sales/", methods=['GET'])
def endpoint_get_sales():
    controller = SalesController(request)
    return controller.list_sales()

@app.route("/sales/<id>/")
def endpoint_get_sales_by_id(id=None):
    controller = SalesController(request)
    return controller.get_sales_by_Id(id)
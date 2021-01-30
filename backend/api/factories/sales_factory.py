from .items_factory import create_items

def create_sales(dbObject):
    return {
        "id": dbObject.id,
        "customers_id": dbObject.customer_id,
        "total": dbObject.total,
        "discount": dbObject.discount,
        "items": [create_items(item) for item in dbObject.items]
    }
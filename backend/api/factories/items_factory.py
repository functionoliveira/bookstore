def create_items(dbObject):
    return {
        "sales_id": dbObject.sales_id,
        "books_id": dbObject.books_id,
        "quantity": dbObject.quantity,
    }
def create_books(dbObject):
    return {
        "id": dbObject.id,
        "title": dbObject.title,
        "author": dbObject.author,
        "unit_price": dbObject.unit_price
    }
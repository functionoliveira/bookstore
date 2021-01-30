def create_customers(dbObject):
    return {
        "id": dbObject.id,
        "fullName": dbObject.fullName,
        "email": dbObject.email,
        "documentType": dbObject.documentType,
        "documentNumber": dbObject.documentNumber,
        "address": dbObject.address
    }
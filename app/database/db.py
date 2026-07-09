from app.models.models import Product, product_to_dict
# Mock database
db = {
    101: Product(id=101, name="Laptop", price=799.99, in_stock=True),
    102: Product(id=102, name="Headphones", price=59.99, in_stock=False)
}

def get_product_by_id(product_id: int):
    prod = db.get(product_id)
    if prod:
        return product_to_dict(prod)
    return None

def update_product_by_id(product_id: int, payload):
    prod = db.get(product_id)
    if prod:
        prod.name = payload.name
        prod.price = payload.price
        prod.in_stock = payload.in_stock
        return product_to_dict(prod)
    return None

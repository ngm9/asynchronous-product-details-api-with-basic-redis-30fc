from typing import Dict
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    in_stock: bool

def product_to_dict(product: Product) -> Dict:
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "in_stock": product.in_stock
    }

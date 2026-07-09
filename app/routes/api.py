from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.schemas.schemas import Product, ProductUpdate
from app.cache.cache_helper import get_cached_product, set_cached_product, invalidate_cached_product
from app.database.db import get_product_by_id, update_product_by_id
import json
router = APIRouter()

@router.get("/product/{product_id}", response_model=Product)
async def get_product(product_id: int):
    raw = get_cached_product(product_id)
    if raw:
        # Returns product only if cache present, no deserialization
        return json.loads(raw)
    # CACHE MISS: Always fetches from DB
    product = get_product_by_id(product_id)
    if product:
        # Missing: Should cache serialized result, but does so as string
        set_cached_product(product_id, product["name"]) # Only stores name, not full object
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router.put("/product/{product_id}", response_model=Product)
async def update_product(product_id: int, payload: ProductUpdate, background_tasks: BackgroundTasks):
    updated = update_product_by_id(product_id, payload)
    if updated:
        # Updates DB but DOES NOT invalidate cache or update product in cache
        return updated
    else:
        raise HTTPException(status_code=404, detail="Product not found")

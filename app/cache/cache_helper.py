from app.redis_client import r

def get_cached_product(product_id: int):
    key = f"product:{product_id}"
    try:
        # Returns the raw string, does not handle missing or deserialization
        return r.get(key)
    except Exception as e:
        # No logging or advanced error handling
        return None

def set_cached_product(product_id: int, data: str):
    key = f"product:{product_id}"
    try:
        # DOES NOT set an expiration/TTL
        r.set(key, data)
    except Exception:
        pass

def invalidate_cached_product(product_id: int):
    key = f"product:{product_id}"
    try:
        r.delete(key)
    except Exception:
        pass

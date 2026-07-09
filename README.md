### Task Overview
This service drives the core product detail page for an ecommerce marketplace. When customers request a product page, the backend fetches details. However, the current system is slow to respond, particularly for popular products, and updates to product data are sometimes not reflected immediately. Frequent database queries for the same products lead to resource spikes and occasional outdated information, frustrating both shoppers and store admins.

# Redis Access

Redis is bound to `127.0.0.1` on the droplet for security and is only accessible from within the droplet itself (via SSH).

**Connection Details:**
- Host: `localhost (127.0.0.1)`
- Port: `6379`

**How to Connect:**

SSH into the droplet and use `redis-cli` directly:
```bash
redis-cli -h 127.0.0.1 -p 6379
```

Or access Redis via the running container:
```bash
docker exec -it <container_name> redis-cli
```

**Useful Commands:**
- View keys: `KEYS *`
- Get a product: `GET product:101`
- View TTL: `TTL product:101`
- Check key type: `TYPE product:101`

### Objectives
- Ensure product detail lookups are at least 50% faster on repeated requests.
- Prevent users from seeing outdated product details after an update.
- Minimize database hits for frequently accessed products by using Redis cache.
- Keep product cache entries fresh and automatically expired after a reasonable time.
- Maintain non-blocking performance and graceful error handling throughout.

### How to Verify
- Request a product detail several times in successionâ€”measure whether repeated requests get faster.
- Use Redis inspection tools to confirm product entries are cached with correct key names and TTLs.
- Update a product, then immediately request its details; verify the updated info appears and cache reflects the change.
- Temporarily stop the Redis container and confirm the API still serves correct product details.
- Verify endpoints remain responsive and non-blocking under normal and degraded (no cache) operation.

### Helpful Tips
- Test the product details endpoint several times for different and repeated product IDs to observe performance changes.
- Use timing tools, browser developer tools, or curl to check API response times before and after your optimizations.
- Think about how frequently accessed product data can be temporarily stored for faster retrieval.
- When a product is updated, verify that new product information is visible to users without long waits.
- Use tools like redis-cli to inspect and verify which keys are stored in Redis, their values, and expiration times.

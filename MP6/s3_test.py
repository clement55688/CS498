import redis

# Replace 'redis://foo.bar.com:12345' with your actual Redis cache URL
redis_url = 'redis://mp6-redis.wf89ar.ng.0001.use1.cache.amazonaws.com:6379'

# Connect to the Redis cache
r = redis.from_url(redis_url)


# Ping the Redis cache
response = r.ping()

# Check the response
if response:
    print("Redis cache is reachable.")
else:
    print("Unable to reach Redis cache.")

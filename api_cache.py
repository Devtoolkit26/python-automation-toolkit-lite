"""
API response cacher — decorator that caches JSON-serializable function output
to disk with configurable TTL. Great for API calls, rate-limited endpoints,
and avoiding re-downloading the same data during development.
"""
import os
import json
import time
import hashlib
from functools import wraps


def cache_api(cache_dir=".cache", ttl=3600):
    """
    Decorator factory. Caches the function's return value (must be JSON-serializable)
    to disk. Cache key is built from the function's name and arguments.

    Args:
        cache_dir: Directory for cache files. Created if missing.
        ttl:       Seconds until a cached entry expires.
    """
    os.makedirs(cache_dir, exist_ok=True)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            raw = f"{func.__name__}{args}{sorted(kwargs.items())}"
            key = hashlib.md5(raw.encode()).hexdigest()
            cache_file = os.path.join(cache_dir, f"{key}.json")

            if os.path.exists(cache_file):
                age = time.time() - os.path.getmtime(cache_file)
                if age < ttl:
                    with open(cache_file) as f:
                        return json.load(f)

            result = func(*args, **kwargs)
            try:
                with open(cache_file, "w") as f:
                    json.dump(result, f)
            except (TypeError, ValueError):
                pass  # Not serializable — skip cache but still return result.
            return result
        return wrapper
    return decorator


# --- Example usage ---

if __name__ == "__main__":
    import requests

    @cache_api(ttl=1800)  # Cache for 30 min
    def fetch_github_user(username):
        r = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        r.raise_for_status()
        return r.json()

    # First call = network. Second call within 30 min = instant from cache.
    print(fetch_github_user("torvalds")["name"])
    print(fetch_github_user("torvalds")["name"])

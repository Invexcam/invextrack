from django.core.cache import cache

def set_cache(key, value, timeout=60*15):
    cache.set(key, value, timeout)

def get_cache(key):
    return cache.get(key)
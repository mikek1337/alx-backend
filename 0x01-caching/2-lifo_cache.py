#!/usr/bin/env python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(last))
            del self.cache_data[last]

    def get(self, key):
        """Gets an item from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

#!/usr/bin/env python3
"""Basic caching module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

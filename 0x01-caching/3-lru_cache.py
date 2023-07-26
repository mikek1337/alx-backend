#!/usr/bin/env python3
"""LRU caching module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.queue[0]]
                print("DISCARD: {}".format(self.queue[0]))
                self.queue.pop(0)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from cache"""
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None

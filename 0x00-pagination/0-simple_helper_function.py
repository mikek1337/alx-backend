#!/usr/bin/env python3
"""simple range indexing module"""


def index_range(page, page_size):
    """finds the index range from page and page_size"""
    return ((page - 1) * page_size, page * page_size)

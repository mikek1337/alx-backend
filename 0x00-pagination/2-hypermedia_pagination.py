#!/usr/bin/env python3
"Module to create page for Popular_Baby_Names"
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        index_ranges = self.index_range(page, page_size)
        if (len(dataset) < index_ranges[1] or len(dataset) < index_ranges[0]):
            return []
        start_index = index_ranges[0]
        end_index = index_ranges[1]
        result = []
        while start_index < end_index:
            result.append(dataset[start_index])
            start_index += 1
        return result

    def index_range(self, page, page_size):
        """finds the index range from page and page_size"""
        return ((page - 1) * page_size, page * page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        current_page = page
        next_page = current_page + 1
        prev_page = current_page - 1
        page_data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.__dataset) / page_size)
        page_info = dict()
        page_info["page_size"] = page_size
        page_info["page"] = current_page
        page_info["data"] = page_data
        if (next_page > total_pages):
            page_info["next_page"] = None
        else:
            page_info["next_page"] = next_page
        if (prev_page <= 0):
            page_info["prev_page"] = None
        else:
            page_info["prev_page"] = prev_page
        page_info["total_pages"] = total_pages
        return page_info

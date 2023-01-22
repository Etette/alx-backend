#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            sel.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive int'
        Args:
            value (int) : the value to be asserted
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        # assert type(page) is int and page > 0
        # assert type(page_size) is int and page_size > 0
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a page of the dataset.
        Args:
            page (int) : the page number
            page_size (int) : the page size
        Returns:
            List[List]: the page of the dataset
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
                "page": page,
                "page_size": page_size if page_size <= len(data) else len(dat),
                "total_pages": total_pages,
                "data": data,
                "prev_page": page - 1 if page > 1 else None,
                "next_page": page + 1 if page + 1 <= total_pages else None
                }
        return info

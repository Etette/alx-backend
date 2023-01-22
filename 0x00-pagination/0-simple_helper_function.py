#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 args and returns a tuple of size 2 containing the
    start and end index corresponding to the range indexes to
    return in a list for those paagination parameters
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Returns:
        Tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)

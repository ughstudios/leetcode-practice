""" Implementation of binary search algorithm """
import math


def _binary_search_helper(items: list[int], left: int, right: int, value: int) -> bool:
    if right >= left:
        middle = math.floor((left + right) / 2)
        if items[middle] == value:
            return True
        elif value > items[middle]:
            return _binary_search_helper(items, middle + 1, right, value)
        elif value < items[middle]:
            return _binary_search_helper(items, left, middle - 1, value)
        else:
            return False


def binary_search_recursive(items: list[int], value: int) -> bool:
    """
    Performs a binary search on a list of sorted items, and returns true if the value exists in the list.
    Uses recursion
    """
    return _binary_search_helper(items, 0, len(items) - 1, value)


def binary_search_iterative(items: list[int], value: int) -> bool:
    """ Iterative implementation of binary search, returns true if the value exists in the list, false otherwise. """
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = math.floor((left + right) / 2)

        if value > items[middle]:
            left = middle + 1
        elif value < items[middle]:
            right = middle - 1
        else:
            return True
    return False

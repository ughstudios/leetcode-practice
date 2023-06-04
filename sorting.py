""" Different implementations of sorting algorithms """
import math


def bubble_sort(items: list) -> list:
    """
    Sorts an input array with the bubble sort algorithm O(N^2) Time Complexity, O(1) Space Complexity
    Stable Sorting Algorithm
    O(N^2) Time
    O(1) Space
    """
    for i in range(len(items) - 1):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def selection_sort(items: list) -> list:
    """
    Sorts an input array using the selection sort algorithm
    O(N^2) Time Complexity
    O(1) Space Complexity
    Unstable Sorting Algorithm
    """
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[min_index] > items[j]:
                min_index = j
        # Swap smallest index value to the beginning with i's current value
        items[i], items[min_index] = items[min_index], items[i]
    return items


def insertion_sort(items: list) -> list:
    """
    Sorts an input array using the insertion sort algorithm O(N^2) avg Time Complexity
    Faster than merge and quick sort for very small input arrays.
    O(N^2) Time Complexity
    O(1) Space Complexity
    Stable Sorting Algorithm
    """
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items


def bucket_sort(items: list) -> list:
    """ Implementation of bucket sort
    Create buckets and distribute elements of array into buckets
    Sort buckets individually
    Merge buckets after sorting
    Number of buckets = round(len(items))
    Appropriate bucket = ceil(value * number_of_buckets / max_value)
    Example: ceil(2*3/9) = ceil(0.6) = 1
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable Sorting Algorithm
    """
    number_of_buckets = round(math.sqrt(len(items)))
    max_value = max(items)
    arr = []

    # Create buckets
    for i in range(number_of_buckets):
        arr.append([])

    # Assign all values to buckets
    for j in items:
        index_b = math.ceil(j * number_of_buckets / max_value)
        arr[index_b - 1].append(j)

    # Sort each bucket individually
    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    # Merge buckets
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            items[k] = arr[i][j]
            k += 1
    return items


def _merge(items: list, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(0, n1):
        left_array[i] = items[left + i]

    for j in range(0, n2):
        right_array[j] = items[middle + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            items[k] = left_array[i]
            i += 1
        else:
            items[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        items[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        items[k] = right_array[j]
        j += 1
        k += 1


def _merge_sort(items: list, left: int, right: int) -> list:
    """ Implementation of merge sort algorithm
    Divide and Conquer algorithm
    Merge halves and sort them
    Divides the array into two halves, recursively calls itself on the two halves and then merges the two halves.
    _merge is for merging the two halves of the array.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable Sorting Algorithm
    """
    if left < right:
        m = (left + (right - 1)) // 2
        _merge_sort(items, left, m)
        _merge_sort(items, m + 1, right)
        _merge(items, left, m, right)
    return items


def merge_sort(items: list) -> list:
    """ Performs a merge sort
    O(n Log n) time complexity
    O(n) space complexity - because of extra arrays (left and right arrays)
     """
    return _merge_sort(items, 0, len(items) - 1)


def _partition(items: list, left: int, right: int):
    """
    Partition method for quick sort algorithm
    Find pivot value
    Loop through all elements and swap if the values are <= the pivot value
    Finally, swap elements that are bigger than the pivot
    :returns Partition Index
    """
    i = left - 1
    pivot = items[right]
    for j in range(left, right):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[right] = items[right], items[i + 1]
    return i + 1


def _quick_sort(items: list, left: int, right: int) -> None:
    """ Quick sort recursive function, used internally (Do not call directly) """
    if left < right:
        pi = _partition(items, left, right)
        _quick_sort(items, left, pi - 1)
        _quick_sort(items, pi + 1, right)


def quick_sort(items: list) -> list:
    """
    Implementation of a quick sort algorithm on a list does not cost extra space complexity unlike merge sort.
    This is also a divide and conquer algorithm like merge sort. QuickSort is not a stable sorting algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    _quick_sort(items, 0, len(items) - 1)
    return items


def _heapify(items: list[int], n: int,  i: int) -> None:
    """ Heapify method for ensuring the list follows heap rules """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and items[i] < items[left]:
        largest = left

    if right < n and items[largest] < items[right]:
        largest = right

    if largest != i:
        items[i], items[largest] = items[largest], items[i]
        _heapify(items, n, largest)


def heap_sort(items: list) -> list:
    """
    Implementation of heap sort algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Unstable sorting algorithm
    """
    n = len(items)
    # Start, stop, step
    for i in range(n // 2 - 1, -1, -1):
        _heapify(items, n, i)

    for i in range(n - 1, 0, -1):
        items[i], items[0] = items[0], items[i]
        _heapify(items, i, 0)
    return items


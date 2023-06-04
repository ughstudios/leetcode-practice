""" Tests sorting algorithms in sorting.py module """
import sorting


def test_bubble_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.bubble_sort(test_data) == sorted(test_data)


def test_selection_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.selection_sort(test_data) == sorted(test_data)


def test_insertion_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.insertion_sort(test_data) == sorted(test_data)


def bucket_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.insertion_sort(test_data) == sorted(test_data)


def test_merge_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.merge_sort(test_data) == sorted(test_data)


def test_quick_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.quick_sort(test_data) == sorted(test_data)


def test_heap_sort() -> None:
    test_data = [5, 9, 100, -111, 2]
    assert sorting.heap_sort(test_data) == sorted(test_data)

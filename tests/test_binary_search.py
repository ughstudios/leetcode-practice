""" Tests binary search """
import binary_search


def test_binary_search() -> None:
    test_data = [1, 2, 3, 4, 5, 6, 9]
    assert binary_search.binary_search_recursive(test_data, 9)
    assert not binary_search.binary_search_recursive(test_data, 100)

    assert binary_search.binary_search_iterative(test_data, 9)
    assert not binary_search.binary_search_iterative(test_data, 100)

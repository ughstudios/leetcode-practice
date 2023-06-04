from heap import Heap, HeapType


def test_min_heap() -> None:
    heap = Heap(HeapType.MIN_HEAP)
    test_data = (5, 1, 10, 15, 20, 25, 30)
    for data in test_data:
        heap.insert(data)

    assert heap.extract() == 1
    assert heap.extract() == 5

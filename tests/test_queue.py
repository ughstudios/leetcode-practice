""" Tests the implementation of the Queue data structure """
from my_queue import Queue


def test_queue():
    my_queue = Queue()
    test_data = [5, 4, 'test']
    assert my_queue.is_empty()
    for value in test_data:
        my_queue.enqueue(value)
    assert not my_queue.is_empty()
    assert my_queue.peak() == test_data[0]
    for i in range(len(test_data)):
        assert test_data[i] == my_queue.dequeue()

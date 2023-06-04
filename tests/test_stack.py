""" Tests for stack implementation """
from stack import Stack


def test_stack():
    test_data = [1, 2, 3, 4, 5, 'test']
    stack = Stack()
    assert stack.is_empty()
    for data in test_data:
        stack.push(data)

    assert not stack.is_empty()
    assert stack.peak() == test_data[-1]

    for i in reversed(range(len(test_data))):
        assert test_data[i] == stack.pop()

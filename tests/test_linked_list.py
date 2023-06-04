""" Tests for linked list implementation """
from linked_list import LinkedList


def test_linked_list():
    linked_list = LinkedList()
    assert linked_list.is_empty()

    test_data = [5, 4, 3, 2, 1]
    for data in test_data:
        linked_list.add(data)
        assert linked_list.search(data)

    assert not linked_list.is_empty()

    linked_list.delete(test_data[-1])
    assert not linked_list.search(test_data[-1])

    linked_list.delete_at(0)
    assert not linked_list.search(test_data[0])

    deletion_position = 1
    linked_list.delete_at(deletion_position)

    temp_node = linked_list.head
    index = 0
    while index < deletion_position - 1:
        temp_node = temp_node.next
        index += 1
    assert temp_node.next.data != test_data[2]


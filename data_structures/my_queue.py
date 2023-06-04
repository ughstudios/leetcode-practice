""" Implementation of a queue data structure (first-in-first-out) """
from __future__ import annotations
from typing import Any, Union
from linked_list import Node, LinkedList


class Queue:
    """ Queue data structure implementation """
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, value: Any) -> None:
        """ Push a new node to the front of the queue """
        node = Node(value)
        if not self.linked_list.head:
            self.linked_list.head = node
            self.linked_list.tail = node
        else:
            # To follow first-in-first-out principles we take the current tail, and set it's next to our new node
            # Then we set the tail to our new node. This makes it so that new values are always added to the
            # end of our linked list/queue, so that the first value dequeued is the first one that was added.
            # When we dequeue, the value at the beginning (our head) is actually the first value we enqueued.
            self.linked_list.tail.next = node
            self.linked_list.tail = node

    def dequeue(self) -> Union[Any, None]:
        """ Returns the node that was just dequeued, or None if there is nothing to return """
        if not self.linked_list.head:
            return

        # To follow first-in-first-out principles, we simply take the head node and store it as a temp variable
        # that will be returned at the end. We then change the head to be the next value in the linked list.
        # This essentially deletes the value from the linked list.
        temp = self.linked_list.head
        self.linked_list.head = self.linked_list.head.next
        return temp.data

    def is_empty(self) -> bool:
        """ Returns true if the queue is empty """
        return self.linked_list.is_empty()

    def peak(self) -> Any:
        """ Returns the top value of the queue without removing it """
        return self.linked_list.head.data

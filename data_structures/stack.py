""" Implementation of stack data structure (last-in-first-out) """
from __future__ import annotations
from typing import Any
from linked_list import Node, LinkedList


class Stack:
    """ Stack implementation using linked list """
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value: Any) -> None:
        """ Push a new item to the top of the stack """
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self) -> Any:
        """ Removes an item from the top of the stack and returns the value """
        if not self.linked_list.head:
            return

        temp_node = self.linked_list.head
        self.linked_list.head = self.linked_list.head.next
        return temp_node.data

    def peak(self) -> Any:
        """ Returns the top element in the stack without removing it """
        if self.linked_list.head:
            return self.linked_list.head.data
        return None

    def is_empty(self) -> bool:
        """  Returns true if the stack is empty """
        return self.linked_list.is_empty()

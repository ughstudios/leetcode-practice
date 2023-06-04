""" Implementation of a singly linked list in python """
from __future__ import annotations
from typing import Any, Union
from dataclasses import dataclass


@dataclass
class Node:
    """ Base Node for Linked Lists """
    data: Any
    next: Union[Node, None] = None

    def __str__(self):
        return str(self.data)


@dataclass
class LinkedList:
    """ Implementation of a linked list """
    head: Union[Node, None] = None
    tail: Union[Node, None] = None

    def is_empty(self) -> bool:
        """ Returns true if we have a linked list head, false otherwise """
        return not self.head

    def add(self, value: Any) -> None:
        """ Adds a new value to a linked list """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, position: int, value: Any) -> None:
        """ Inserts a value at a position """
        if not self.head:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            new_node = Node(value)
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            elif position == -1:
                # Insert at the end of the linked list
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def search(self, value: int) -> bool:
        """ Returns true if the value is found in the linked list """
        if not self.head:
            return False
        if isinstance(self.head, Node) and self.head.data == value:
            return True
        if isinstance(self.tail, Node) and self.tail.data == value:
            return True

        temp_node = self.head.next
        while temp_node:
            if temp_node.data == value:
                return True
            else:
                temp_node = temp_node.next
        return False

    def delete(self, value: Any) -> None:
        """ Removes the first instance of any value in the linked list """
        if not self.head:
            return
        if isinstance(self.head, Node) and self.head.data == value:
            temp_node = self.head
            temp_node.next = temp_node.next.next
        if isinstance(self.tail, Node) and self.tail.data == value:
            self.tail = None

        temp_node = self.head
        temp_node2 = self.head.next
        while temp_node or temp_node2:
            if temp_node2.data == value:
                temp_node.next = temp_node.next.next
            temp_node = temp_node.next
            temp_node2 = temp_node2.next

    def delete_at(self, position: int) -> None:
        """ Removes value at a location """
        if position == 0:
            self.head = self.head.next
            return

        temp_node = self.head
        index = 0
        while index < position - 1:
            temp_node = temp_node.next
            index += 1
        temp_node.next = temp_node.next.next

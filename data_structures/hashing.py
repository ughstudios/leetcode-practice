""" Implementation of hash tables and basic hashing methods """
from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass


def _mod(number: int, cell_number: int) -> int:
    """ Do not use in a production system, these are just examples """
    return number % cell_number


def _mod_ascii(string: str, cell_number) -> int:
    """ Do not use in a production system, these are just examples """
    total = 0
    for i in string:
        total += ord(i)
    return total % cell_number


@dataclass
class HashNode:
    key: Any
    value: Any
    next: HashNode = None

    def __len__(self):
        i = 0
        current_node = self
        while current_node.next is not None:
            i += 1
            current_node = current_node.next
        return i


class HashTable:
    """ Basic implementation of a hash table using direct chaining for collision """
    def __init__(self, max_size = 255):
        self.max_size = max_size
        self.table: list[Optional[HashNode]] = [None] * self.max_size

    def get(self, key: Any) -> Any:
        """ Gets a value from the hash table """
        index = self._hasher(key)
        if len(self.table[index]) == 1:
            return self.table[index].value
        else:
            current_node = self.table[index]
            while current_node.key != key:
                current_node = current_node.next

            if current_node.key == key:
                return current_node.value
            else:
                return None

    def _hasher(self, key: Any) -> int:
        return hash(key) % self.max_size

    def is_full(self) -> bool:
        """ Returns true if the hash table is full and all buckets are used up """
        for kvp in self.table:
            if not kvp:
                return False
        return True

    def put(self, key: Any, value: Any):
        """ Inserts a key value pair into the hash table """
        index = self._hasher(key)
        if not self.table[index]:
            self.table[self._hasher(key)] = HashNode(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = HashNode(key, value)

    def delete(self, key: Any):
        """ Deletes a key and it's value from the hash table """
        index = self._hasher(key)
        if not self.table[index]:
            return
        else:
            if len(self.table[index]) == 1:
                self.table[index] = None
            else:
                if self.table[index].key == key:
                    self.table[index] = self.table[index].next
                    return
                else:
                    current_node = self.table[index]
                    next_node = self.table[index].next
                    while current_node.next is not None:
                        if next_node.key == key:
                            current_node.next = current_node.next.next
                            return
                        current_node = current_node.next
                        next_node = next_node.next

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

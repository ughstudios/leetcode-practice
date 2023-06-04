""" Implementation of min and max heaps """
from enum import Enum


class HeapType(Enum):
    """ Enum for defining the type of heap to be created """
    MIN_HEAP = 1
    MAX_HEAP = 2


class Heap:
    def __init__(self, heap_type: HeapType, size: int = 100):
        self.values = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1
        self.heap_type = heap_type

    def peek(self) -> int:
        """ Look at the max value within the heap without removing it """
        return self.values[1]

    def size(self):
        """ Get the number of values in the heap """
        return self.heap_size

    def level_order_traversal(self) -> None:
        for i in range(1, self.heap_size + 1):
            print(self.values[i])

    def heapify_insert(self, index: int) -> None:
        parent_index = int(index / 2)
        if index <= 1:
            return
        if self.heap_type == HeapType.MIN_HEAP:
            if self.values[index] < self.values[parent_index]:
                temp = self.values[index]
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = temp
            self.heapify_insert(parent_index)
        elif self.heap_type == HeapType.MAX_HEAP:
            if self.values[index] > self.values[parent_index]:
                temp = self.values[index]
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = temp
            self.heapify_insert(parent_index)

    def insert(self, value: int) -> None:
        """ Inserts a value into a heap """
        if self.heap_size + 1 >= self.max_size:
            raise Exception('heap "size" reached.')
        self.values[self.heap_size + 1] = value
        self.heap_size += 1
        self.heapify_insert(self.heap_size)

    def heapify_extract(self, index: int) -> None:
        left_index = index * 2
        right_index = index * 2 + 1
        if self.heap_size < left_index:
            return
        elif self.heap_size == left_index:
            if self.heap_type == HeapType.MIN_HEAP:
                if self.values[index] > self.values[left_index]:
                    temp = self.values[index]
                    self.values[index] = self.values[left_index]
                    self.values[left_index] = temp
                return
            else:
                if self.values[index] < self.values[left_index]:
                    temp = self.values[index]
                    self.values[index] = self.values[left_index]
                    self.values[left_index] = temp
                return
        else:
            if self.heap_type == HeapType.MIN_HEAP:
                if self.values[left_index] < self.values[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.values[index] > self.values[swap_child]:
                    temp = self.values[index]
                    self.values[index] = self.values[swap_child]
                    self.values[swap_child] = temp
            else:
                if self.values[left_index] < self.values[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.values[index] < self.values[swap_child]:
                    temp = self.values[index]
                    self.values[index] = self.values[swap_child]
                    self.values[swap_child] = temp
        self.heapify_extract(swap_child)

    def extract(self) -> int:
        """ Returns the max or min value from the heap and removes it from the heap """
        if self.heap_size == 0:
            return
        else:
            value = self.values[1]
            self.values[1] = self.values[self.heap_size]
            self.values[self.heap_size] = None
            self.heap_size -= 1
            self.heapify_extract(1)
            return value

    def reset_heap(self) -> None:
        """ Resets all the values in the heap to None """
        self.values = self.max_size * [None]

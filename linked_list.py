from __future__ import annotations
from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    data: Any
    next: Node = None


n1 = Node('test')
n2 = Node('test2')
n1.next = n2

curr_node = n1
while curr_node:
    print(curr_node.data)
    curr_node = curr_node.next


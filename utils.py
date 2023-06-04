from __future__ import annotations
from typing import Any


class TreeNode:
    def __init__(self, value: int = 0, left: TreeNode = None, right: TreeNode = None) -> None:
        self.value = value
        self.left = left
        self.right = right        


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(linked_list: ListNode) -> None:
    node = linked_list
    list_values = []
    while node:
        list_values.append(str(node.val))
        node = node.next
    print(' '.join(list_values))


def convert_list_to_linkedlist(list_to_convert: list[Any]) -> ListNode:
    first_node = list_to_convert.pop(0)
    head = ListNode(first_node)
    current_node = head
    while list_to_convert:
        popped = list_to_convert.pop(0)
        current_node.next = ListNode(popped)
        current_node = current_node.next
    return head

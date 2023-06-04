# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(N) time and space because we store each value in the values array. 
def is_palindrome(head: Optional[ListNode]) -> bool:
    values = []
    current_node = head
    while current_node:
        values.append(current_node.val)
        current_node = current_node.next
    return values == list(reversed(values))
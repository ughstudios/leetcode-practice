# https://leetcode.com/problems/linked-list-cycle/
# https://leetcode.com/problems/linked-list-cycle/discuss/1829489/C%2B%2B-oror-Easy-To-Understand-oror-2-Pointer-oror-Fast-and-Slow

from typing import Optional


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


# O(N) Space Complexity
def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    current_node = head
    values = set()
    while current_node != None:
        if current_node in values:
            return True
        
        values.add(current_node)
        current_node = current_node.next
    return False


# O(1) Space complexity
def has_cycle(head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if not node.val:
                return True
            node.val = None
            node = node.next
        return False

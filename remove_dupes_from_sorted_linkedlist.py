# https://leetcode.com/problems/remove-duplicates-from-sorted-list
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # If the head or it's next node is empty, just return the head. As it's impossible for there to be any dupes. 
    if not head or not head.next:
        return head
    
    node = head
    # Go through each node
    while node.next:
        # If the current nodes value is equal to it's next value, remove it.
        # This works because it's a sorted linked list so all values that are the same will be right next to each other. 
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
            
    return head

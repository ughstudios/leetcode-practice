# https://leetcode.com/problems/remove-linked-list-elements/
from typing import Optional
from utils import convert_list_to_linkedlist


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Remove all of the elements matching the value from the beginning of the linked list by moving the head up one at a time. 
        while head and head.val == val:
            head = head.next
        
        current_node = head
        while current_node and current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head


head = convert_list_to_linkedlist([1,2,6,3,4,5,6])
value_to_remove = 6
remove_elements(head, value_to_remove)

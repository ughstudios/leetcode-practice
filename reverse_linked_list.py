# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
from utils import convert_list_to_linkedlist, print_linked_list


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # If there is no head or the next value is empty that means we have no list, or it's a list with one element.
    if not head or not head.next:
        return head
    
    # Recursively will go all the way to the end of the linked list until there is no more "next" nodes
    # Once there is no more next nodes found, it will use that as the head. 
    new_head = reverse_list(head.next)

    head.next.next = head
    head.next = None
    
    return new_head




test_data = [1, 2, 3, 4, 5]
linked_list = convert_list_to_linkedlist(test_data)
print_linked_list(linked_list)
new_linkedlist = reverse_list(linked_list) # Reverse list is effecting the original list
print_linked_list(new_linkedlist)

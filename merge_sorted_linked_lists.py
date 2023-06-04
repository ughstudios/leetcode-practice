# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional
from utils import ListNode, convert_list_to_linkedlist, print_linked_list


def merge_two_sorted_linked_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    
    tail.next = list1 or list2
    return dummy.next



test_data = [1, 2, 3, 4, 5]
test_data2 = [1, 2, 3, 4, 5]

list1 = convert_list_to_linkedlist(test_data)
list2 = convert_list_to_linkedlist(test_data2)

print_linked_list(list1)
print_linked_list(list2)
print_linked_list(merge_two_sorted_linked_lists(list1, list2))
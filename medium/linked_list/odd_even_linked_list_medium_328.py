from typing import Optional
from utils import ListNode, build_linked_list, print_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        even = ListNode()
        odd = ListNode()
        head_odd = odd

        i = 0
        while head:
            if i % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next

            head = head.next
            i = i + 1

        odd.next = None
        even.next = head_odd.next

        return root


head = [1,2,3,4,5]
listNode = build_linked_list(head)

res = Solution().oddEvenList(listNode)
print_linked_list(res)

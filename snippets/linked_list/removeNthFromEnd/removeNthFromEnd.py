# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Tools.scripts.pep384_macrocheck import dprint

from snippets.linked_list.linked_list_utils import ListNode, display, list_to_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n+1):
            fast = fast.next


        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
head = [1, 2, 3, 4, 5]
n = 2

display(Solution().removeNthFromEnd(list_to_linked_list(head), n))
# display(list_to_linked_list(head))

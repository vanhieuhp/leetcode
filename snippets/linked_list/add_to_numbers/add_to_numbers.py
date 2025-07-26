# Definition for singly-linked list.
from typing import Optional

from snippets.linked_list.linked_list_utils import ListNode, display
from snippets.linked_list.linked_list_utils import list_to_linked_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

# output [7,0,8]


l1 = list_to_linked_list(l1)
l2 = list_to_linked_list(l2)
display(Solution().addTwoNumbers(l1, l2))




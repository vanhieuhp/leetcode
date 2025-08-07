# Definition for singly-linked list.
from typing import Optional

from utils import ListNode, build_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        while head:
            node = ListNode(head.val)
            node.next = current
            head = head.next
            current = node
        return current


head = [1, 2, 3, 4, 5]
res = Solution().reverseList(build_linked_list(head))
print_linked_list(res)
# print_linked_list(build_linked_list(head))

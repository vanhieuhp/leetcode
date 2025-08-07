from typing import Optional

from utils import ListNode, print_linked_list, build_linked_list


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head

        h_len = 0
        while head:
            h_len += 1
            head = head.next
        if h_len < 2:
            return None

        middle = h_len // 2
        head = root

        while middle > 1:
            head = head.next
            middle = middle - 1

        if head.next:
            head.next = head.next.next

        return root


head = [1, 3, 4, 7, 1, 2, 6]
listNode = build_linked_list(head)
res = Solution().deleteMiddle(listNode)
print_linked_list(res)

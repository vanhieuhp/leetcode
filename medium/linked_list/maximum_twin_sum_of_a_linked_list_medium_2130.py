from typing import Optional
from utils.linked_list_utils import ListNode, build_linked_list


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        sum_list = []
        left, right = 0, len(val_list) - 1
        while left < right:
            total = val_list[left] + val_list[right]
            left = left + 1
            right = right - 1
            sum_list.append(total)

        return max(sum_list)

head = [5, 4, 2, 1]
head = build_linked_list(head)
res = Solution().pairSum(head)

print(res)

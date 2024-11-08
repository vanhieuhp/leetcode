from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif gas < n:
                gas = n

            gas -= 1

        return True

    def jump(self, nums: List[int]) -> int:
        min_tep = 0
        gas = 0
        for n in nums:
            if gas < 0:
                return -1
            elif gas < n:
                gas = n
                min_tep += 1

            gas -= 1

        return min_tep


# nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
nums = [2, 3, 1, 1, 4]
# nums = [0, 2, 3]
# print(Solution().canJump(nums))

print(Solution().jump(nums))

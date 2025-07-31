from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for i in range(0, len(nums)):
            right_sum = right_sum - nums[i]
            if left_sum == right_sum:
                return i

            left_sum = left_sum + nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
res = Solution().pivotIndex(nums)
print(res)

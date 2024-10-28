from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            if i == 0:
                sum = nums[i]
            temp = []
            temp_sum = 0
            if sum >= 0 and nums[i] < 0:
                continue
            for j in range(i, len(nums)):
                temp.append(nums[j])
                temp_sum += nums[j]
                if sum < temp_sum:
                    sum = temp_sum

        return sum


nums = [-2, 1, -3, 4, -1, 2, -1, 5, 4]
# Output: 6
print(Solution().maxSubArray(nums))

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        left, right, count = 0, len(nums) - 1, 0

        nums.sort()

        while left < right:
            total = nums[left] + nums[right]

            if total == k:
                count += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1

        return count


nums = [3, 1, 3, 4, 3]
k = 6
result = Solution().maxOperations(nums, k)

print(result)

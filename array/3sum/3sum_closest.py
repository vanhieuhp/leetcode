from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float("inf")
        n = len(nums)

        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if target == total:
                    return target

                if abs(total - target) <= abs(result - target):
                    result = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return result


nums = [-1, 2, 1, -4]
target = 1

print(Solution().threeSumClosest(nums, target))

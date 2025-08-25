from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # peak is on the right
                left = mid + 1
            else:
                # peak is on the left or mid
                right = mid
        
        return left


nums = [1,2,1,3,5,6,4]
res = Solution().findPeakElement(nums)
print(res)

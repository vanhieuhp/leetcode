from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0

nums = [0,1,0,3,12] # 1,3,12,0,0
# 0,0,0,1,0,1,3
# 1,2,0,1,0,3
# nums = [1,2,0,1,0,3]
Solution().moveZeroes(nums)

print(nums )
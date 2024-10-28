"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if len(nums) <= 1:
            return [nums]
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            perms = self.permuteUnique(sub_array(i, nums[:]))
            for perm in perms:
                result.append(perm + [nums[i]])
            i += 1
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) <= 1:
            return [nums]

        for i in range(0, len(nums)):
            perms = self.permute(sub_array(i, nums[:]))
            for perm in perms:
                result.append(perm + [nums[i]])

        return result

def sub_array(i, nums):
    nums.pop(i)
    return nums


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
# print(sub_array(3, nums))

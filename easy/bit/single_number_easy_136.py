from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        
        return res


# nums = [2, 2, 1]
nums = [4,1,2,1,2]

res = Solution().singleNumber(nums)
print(res)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 # dp[i-2]
        prev1 = 0 # dp[i-1]
        for x in nums:
            temp = prev2 + x

            prev2 = prev1
            prev1 = max(prev1, temp)

        return prev1

nums = [2,1,1,2]
res = Solution().rob(nums)
print(res)
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num < first:
                first = num # the smallest so far
            elif num < second:
                second = num
            else:
                return True
            
        return False


# nums = [1,2,3,4,5]
nums = [20, 100, 10, 12, 5, 13]
# nums = [5,4,3,2,1]

# 1, 2, 6, 2, 7
# 2, 1, 5, 0, 4, 6

result = Solution().increasingTriplet(nums)
print(result)

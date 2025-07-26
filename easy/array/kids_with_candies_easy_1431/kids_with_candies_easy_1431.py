from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # result = []
        the_greatest = max(candies)
        return [c + extraCandies >= the_greatest for c in candies]
        # for candidie in candies:
        #     if candidie + extraCandies >= the_greatest:
        #         result.append(True)
        #     else:
        #         result.append(False)
        #
        # return result

# candies = [2, 3, 5, 1, 3]
# extraCandies = 3

# candies = [4,2,1,1,2]
# extraCandies = 1
#
# candies = [12, 1, 12]
# extraCandies = 10
result = Solution().kidsWithCandies(candies, extraCandies)
print(result)

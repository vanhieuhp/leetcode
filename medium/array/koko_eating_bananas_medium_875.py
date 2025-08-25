from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        ans = right

        def can_finish(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1 # try smaller k
            else:
                left = mid + 1

        return ans
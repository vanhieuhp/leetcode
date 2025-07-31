from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        sum_al = 0
        for al in gain:
            sum_al = sum_al + al
            res = max(sum_al, res)

        return res

gain = [-5, 1, 5, 0, -7]

res = Solution().largestAltitude(gain)
print(res)
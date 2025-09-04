from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

n = 2
res = Solution().countBits(n)
print(res)
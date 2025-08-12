import math
from typing import List

MOD = 10**9 + 7

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        # 1) build list of powers i^x <= n
        powers: List[int] = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            # iterate backwards to avoid reuse of the same power multiple times
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD
        return dp[n]
n = 4
x = 1
res = Solution().numberOfWays(n, x)
print(res)
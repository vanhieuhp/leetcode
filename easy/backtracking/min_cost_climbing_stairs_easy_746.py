from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first, second = cost[0], cost[1]

        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first, second = second, curr

        return min(first, second)


cost = [10, 15, 20]
res = Solution().minCostClimbingStairs(cost)
print(res)

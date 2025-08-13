from collections import defaultdict, Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total_count = count1 + count2

        for fruit, cnt, in total_count.items():
            if cnt %2 != 0:
                return -1

        min_fruit = min(total_count.keys())
        excess = []

        # build the excess list
        for fruit in total_count:
            if count1[fruit] == count2[fruit]:
                continue
            diff = int(count1[fruit] - count2[fruit] // 2)
            excess.append(fruit * abs(diff))

        excess.sort()
        swaps_needed = len(excess) // 2

        cost = 0
        for i in range(swaps_needed):
            cost += min(excess[i], min_fruit * 2)

        return cost

basket1 = [84, 80, 43, 8, 80, 88, 43, 14, 100, 88]
basket2 = [32, 32, 42, 68, 68, 100, 42, 84, 14, 8]

# basket1 = [4,2,2,2]
# basket2 = [1,4,1,2]

res = Solution().minCost(basket1, basket2)
print(res)

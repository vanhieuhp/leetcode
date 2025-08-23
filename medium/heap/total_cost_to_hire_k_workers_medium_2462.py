from typing import List
import heapq
from collections import defaultdict, Counter,  deque


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
       
        min_priority_heap = []
        left, right = 0, len(costs) - 1

        if candidates * 2 <= len(costs):
            for i in range(candidates):
                heapq.heappush(min_priority_heap, (costs[left], left))
                heapq.heappush(min_priority_heap, (costs[right], right))
                left +=1
                right -=1

        while k > 0 and candidates * 2 < len(costs) and left <= right:
            cost, index = heapq.heappop(min_priority_heap)
            total_cost += cost
            if index < left:
                heapq.heappush(min_priority_heap, (costs[left], left))
                left += 1
            else:
                heapq.heappush(min_priority_heap, (costs[right], right))
                right -= 1
        
            k -= 1

        if k > 0:
            while left <= right:
                heapq.heappush(min_priority_heap, (costs[left], left))
                left += 1

        while k > 0:
            cost, index = heapq.heappop(min_priority_heap)
            total_cost += cost
            k -= 1
        
        return total_cost

costs = [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34]
k = 32
candidates = 12
res = Solution().totalCost(costs, k, candidates)
print(res)

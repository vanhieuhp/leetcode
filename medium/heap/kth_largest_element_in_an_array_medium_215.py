from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        while k > 1:
            heapq.heappop(max_heap)
            k -=1
        return -heapq.heappop(max_heap)


nums = [3, 2, 1, 5, 6, 4]
k = 2
res = Solution().findKthLargest(nums, k)
print(res)
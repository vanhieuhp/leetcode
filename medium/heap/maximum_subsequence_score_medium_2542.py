from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        total = 0
        result = 0

        for num2, num1 in pairs:
            # add nums1 value into heap
            heapq.heappush(heap, num1)
            total += num1

            # keep only k elements
            if len(heap) > k:
                total -= heapq.heappop(heap)

            # if we already selected k elements, compute score
            if len(heap) == k:
                result = max(result, total * num2)

        return result



nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
res = Solution().maxScore(nums1, nums2, k)
print(res)

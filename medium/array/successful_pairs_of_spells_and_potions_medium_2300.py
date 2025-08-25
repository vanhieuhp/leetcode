from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        def bisect_left(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (right + left) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for s in spells:
            threshold = (success + s - 1) // s
            idx = bisect_left(potions, threshold)
            res.append(m-idx)

        return res
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7

res = Solution().successfulPairs(spells, potions, success)
print(res)
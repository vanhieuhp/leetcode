from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = dict()

        for num in arr:
            occurs[num] = occurs.get(num, 0) + 1

        return  len(set(occurs.values())) == len(set(occurs.keys()))

arr = [1,2,2,1,1,3]

res = Solution().uniqueOccurrences(arr)
print(res)
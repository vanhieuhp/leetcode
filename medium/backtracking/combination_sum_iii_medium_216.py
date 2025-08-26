from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k < 1:
            return 0

        result = []

        def backtrack(start: int, path: List[int], remaining: int):

            if len(path) == k:
                if remaining == 0:
                    result.append(path.copy())
                return

            for i in range(start, 10):
                if i > remaining:
                    break
                path.append(i)

                backtrack(i + 1, path, remaining - i)
                path.pop()

        backtrack(1, [], n)
        return result

k = 3
n = 9

res = Solution().combinationSum3(k, n)
print(res)
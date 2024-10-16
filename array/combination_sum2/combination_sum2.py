from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1

            dfs(i + 1, cur, total)

        candidates.sort()
        res = []
        dfs(0, [], 0)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
#
# candidates = [2, 5, 2, 1, 2]
# target = 5
#
# candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# target = 30
# print(len(candidates))
print(Solution().combinationSum2(candidates, target))

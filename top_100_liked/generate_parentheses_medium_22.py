from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current, left, right):
            # base case
            if len(current) == n * 2:
                res.append(current)
                return

            if left < n:
                backtrack(current + "(", left + 1, right)

            if right < left:
                backtrack(current + ")", left, right + 1)

        backtrack("", 0, 0)

        return res


n = 3
res = Solution().generateParenthesis(n)
print(res)
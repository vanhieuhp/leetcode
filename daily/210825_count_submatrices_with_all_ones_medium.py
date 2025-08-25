from typing import List
import datetime

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        heights = [0] *  cols
        result = 0

        for r in range(rows):
            # build histogram heights for this now
            for c in range(cols):
                if mat[r][c] == 0:
                    heights[c] = 0
                else:
                    heights[c] += 1

            # count submatrices using heights
            stack = []
            sum_in_row = [0] * cols
            for c in range(cols):
                while stack and heights[stack[-1]] >= heights[c]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    sum_in_row[c] = sum_in_row[prev] + heights[c] * (c-prev)
                else:
                    sum_in_row[c] = heights[c] * (c+1)

                stack.append(c)
                result += sum_in_row[c]

        return result

mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]

start = datetime.datetime.now()
res = Solution().numSubmat(mat)
end = datetime.datetime.now()
print(res)
print("end - start:", end - start, "seconds")
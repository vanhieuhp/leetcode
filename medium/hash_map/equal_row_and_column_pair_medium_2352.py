from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        len_grid = len(grid)

        dict_row = dict()
        dict_col = dict()
        for i in range(len_grid):
            row = ",".join(str(cell) for cell in grid[i])
            dict_row[row] = dict_row.get(row, 0) + 1

            arr_col = []
            for j in range(len_grid):
                arr_col.append(str(grid[j][i]))
            col = ",".join(arr_col)
            dict_col[col] = dict_col.get(col, 0) + 1


        count = 0
        for k, v in dict_row.items():
            count += dict_row.get(k) * dict_col.get(k, 0)

        return count

grid = [[11,1],[1,11]]
res = Solution().equalPairs(grid)
print(res)

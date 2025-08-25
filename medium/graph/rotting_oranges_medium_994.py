from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        q = deque()
        fresh_oranges = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            cr, cc, step = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + cr, cc + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append([nr, nc, step + 1])

                if fresh_oranges <= 0:
                    return step

        return -1


grid = [[0,2]]
res = Solution().orangesRotting(grid)
print(res)

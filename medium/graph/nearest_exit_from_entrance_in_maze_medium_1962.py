from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        # BFS queue
        q = deque([(entrance[0], entrance[1], 0)])

        maze[entrance[0]][entrance[1]] = "+"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # row-column

        while q:
            row, col, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':

                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1

                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1


maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

res = Solution().nearestExit(maze, entrance)
print(res)

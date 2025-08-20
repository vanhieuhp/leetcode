from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # build adjacency list with direction info
        # stone (neighbor, needs_flip)
        for a, b in connections:
            graph[a].append((b, 1)) # edge a->b (points away from 0, may need flip)
            graph[b].append((a, 0)) # edge b->a (already towards 0)

        visited = set()
        changes = 0

        def dfs(city):
            nonlocal changes
            visited.add(city)
            for neighbor, needs_flip in graph[city]:
                if neighbor not in visited:
                    changes += needs_flip
                    dfs(neighbor)

        dfs(0)
        return changes
        

n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
res = Solution().minReorder(n, connections)
print(res)
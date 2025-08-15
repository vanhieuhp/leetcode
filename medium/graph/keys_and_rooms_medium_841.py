from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0] # use list as a stack for DFS
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)
        

rooms = [[1,3],[3,0,1],[2],[0]]

res = Solution().canVisitAllRooms(rooms)
print(res)
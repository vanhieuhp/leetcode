from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        res = 1

        prevEnd = points[0][1]
        bound = prevEnd
        for start, end in points[1:]:
            if start > prevEnd or start > bound:
                prevEnd = end
                res += 1
                bound = end
            else:
                bound = min(bound, end)

        return res

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
res = Solution().findMinArrowShots(points)
print(res)
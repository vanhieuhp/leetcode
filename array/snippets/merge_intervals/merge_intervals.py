from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        result = []
        first = intervals[0]

        for i in range(1, len(intervals)):
            second = intervals[i]
            temp = []
            if first[-1] >= second[0]:
                temp.append(min(first[0], second[0]))
                temp.append(max(first[-1], second[-1]))
                first = temp[:]
            else:
                result.append(first)
                first = second[:]

        return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(intervals))

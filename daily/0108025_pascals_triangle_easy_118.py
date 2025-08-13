from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        res = [[1]]

        for i in range(1, numRows):
            prev = [0] + res[-1] + [0]
            
            row = []
            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j + 1])
            res.append(row)

        return res


numRows = 5
res = Solution().generate(numRows)

print(res)
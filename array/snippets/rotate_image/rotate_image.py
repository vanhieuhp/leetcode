from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            new_array = []
            for j in range(n - 1, -1, -1):
                new_array.append(matrix[j][i])
            matrix.append(new_array)

        for i in range(n):
            matrix.pop(0)

    def rotate_v2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Solution().rotate(matrix)
Solution().rotate_v2(matrix)
print(matrix)

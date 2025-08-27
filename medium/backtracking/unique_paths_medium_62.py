class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * (n+1) for _ in range(m+1)]
        arr[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                arr[i][j] = arr[i][j] + arr[i][j+1] + arr[i+1][j]

        return arr[0][0]

m = 3
n = 7
res = Solution().uniquePaths(m, n)
print(res)
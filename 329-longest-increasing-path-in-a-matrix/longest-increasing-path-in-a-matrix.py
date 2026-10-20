class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def solve(i, j):
            c1 = c2 = c3 = c4 = 0
            if i > 0:
                if matrix[i - 1][j] > matrix[i][j]:
                    c1 = solve(i - 1, j)
            if i < m - 1:
                if matrix[i + 1][j] > matrix[i][j]:
                    c2 = solve(i + 1, j)
            if j > 0:
                if matrix[i][j - 1] > matrix[i][j]:
                    c3 = solve(i, j - 1)
            if j < n - 1:
                if matrix[i][j + 1] > matrix[i][j]:
                    c4 = solve(i, j + 1)
            return 1 + max(c1, c2, c3, c4)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, solve(i, j))
        return ans
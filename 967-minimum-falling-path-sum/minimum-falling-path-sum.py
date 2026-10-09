class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        @cache
        def fun(i,j):
            if i<0 or i>=len(matrix):
                return float("inf")
            if j<0 or j>=len(matrix[0]):
                return float("inf")
            if i==len(matrix)-1:
                return matrix[i][j]
            c1 = matrix[i][j]+fun(i+1,j)
            c2 = matrix[i][j]+fun(i+1,j+1)
            c3 = matrix[i][j]+fun(i+1,j-1)
            return min(c1,c2,c3)
        ans = float("inf")
        for j in range(len(matrix[0])):
            ans = min(ans,fun(0,j))
        return ans
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def fun(i,j):
            if i>=m or j>=n or obstacleGrid[i][j] == 1:
                return 0
            if i==m-1 and j ==n-1:
                return 1
            c1 = fun(i+1,j)
            c2 = fun(i,j+1)
            return c1+c2
        return fun(0,0)
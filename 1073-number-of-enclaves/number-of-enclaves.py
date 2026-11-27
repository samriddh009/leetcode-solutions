class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n= len(grid)
        m = len(grid[0])
        vis=[[0]*m for _ in range(n)]
        count = sum(row.count(1) for row in grid)
        def fun(i,j):
            vis[i][j]=1
            nonlocal count
            count-=1
            if i-1>=0 and grid[i-1][j]==1 and vis[i-1][j]==0:
                fun(i-1,j)
            if i+1<n and grid[i+1][j]==1 and vis[i+1][j]==0:
                fun(i+1,j)
            if j-1>=0 and grid[i][j-1]==1 and vis[i][j-1]==0:
                fun(i,j-1)
            if j+1<m and grid[i][j+1]==1 and vis[i][j+1]==0:
                fun(i,j+1)
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==1 and vis[i][j]==0:
                    fun(i,j)
        return count

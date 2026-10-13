class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m,n =len(grid),len(grid[0])
        vis=[[False]*n for _ in range(m)]
        cnt= 0
        x=y= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    cnt+=1
                if grid[i][j]==1:
                    x,y = i,j
        def fun(i, j, rem):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if grid[i][j]==-1 or vis[i][j]:
                return 0
            if grid[i][j]==2:
                if rem==1:
                    return 1 
                else:
                    return 0
            vis[i][j] = True
            ans = (fun(i-1,j,rem-1)+ fun(i+1,j,rem-1)+ fun(i,j-1,rem-1)+ fun(i,j+1,rem-1))
            vis[i][j] = False
            return ans
        return fun(x, y, cnt)
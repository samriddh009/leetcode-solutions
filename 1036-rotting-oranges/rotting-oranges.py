class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        t= 0
        while q and fresh:
            for _ in range(len(q)):
                x,y = q.popleft()
                if x-1>=0 and grid[x-1][y]==1:
                    grid[x-1][y]=2
                    fresh-=1
                    q.append((x-1,y))
                if x+1<n and grid[x+1][y]==1:
                    grid[x+1][y]=2
                    fresh-=1
                    q.append((x+1,y))
                if y-1>=0 and grid[x][y-1]==1:
                    grid[x][y-1]=2
                    fresh-=1
                    q.append((x,y-1))
                if y+1<m and grid[x][y+1]==1:
                    grid[x][y+1]=2
                    fresh-=1
                    q.append((x,y+1))
            t+=1
        return t if fresh==0 else -1
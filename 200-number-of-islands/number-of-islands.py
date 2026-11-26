class Solution:
    def numIslands(self, graph: List[List[str]]) -> int:
        n = len(graph)
        m = len(graph[0])
        vis = [[0]*m for i in range(n)]
        count = 0
        def dfs(i,j):
            vis[i][j]=1
            if i-1>=0 and graph[i-1][j]=="1" and vis[i-1][j]==0:
                dfs(i-1,j)
            if i+1<n and graph[i+1][j]=="1" and vis[i+1][j]==0:
                dfs(i+1,j)
            if j-1>=0 and graph[i][j-1]=="1" and vis[i][j-1]==0:
                dfs(i,j-1)
            if j+1<m and graph[i][j+1]=="1" and vis[i][j+1]==0:
                dfs(i,j+1)
        for i in range(n):
            for j in range(m):
                if graph[i][j]=="1" and vis[i][j]==0:
                    dfs(i,j)
                    count+=1
        return count
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        vis = [0]*V
        res = []
        def dfs(i,arr):
            vis[i]=1
            arr.append(i)
            for j in range(V):
                if isConnected[i][j] == 1 and vis[j] == 0:
                    dfs(j,arr)
        for i in range(V):
            if vis[i]==0:
                arr=[]
                dfs(i,arr)
                res.append(arr)
        return len(res)
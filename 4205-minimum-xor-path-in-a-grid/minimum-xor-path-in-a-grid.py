from functools import cache

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def fun(i, j):
            if i == m - 1 and j == n - 1:
                return frozenset([grid[i][j]])
                
            res = set()
            if i + 1 < m:
                for val in fun(i + 1, j):
                    res.add(grid[i][j] ^ val)
            if j + 1 < n:
                for val in fun(i, j + 1):
                    res.add(grid[i][j] ^ val)
                    
            return frozenset(res)
            
        return min(fun(0, 0))
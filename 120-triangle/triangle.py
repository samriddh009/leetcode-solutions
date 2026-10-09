class Solution:
    def minimumTotal(self, grid: list[list[int]]) -> int:
        @cache
        def fun(i,j):
            if i==len(grid)-1:
                return grid[i][j]
            c1 = grid[i][j]+fun(i+1,j)
            c2 = grid[i][j]+fun(i+1,j+1)
            return min(c1,c2)
        return fun(0,0)
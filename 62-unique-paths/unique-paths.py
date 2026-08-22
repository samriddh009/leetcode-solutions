@cache
def fun(i,j,m,n):
    if i>=m or j>=n:
        return 0
    if i==m-1 and j ==n-1:
        return 1
    c1 = fun(i+1,j,m,n)
    c2 = fun(i,j+1,m,n)
    return c1+c2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fun(0,0,m,n)
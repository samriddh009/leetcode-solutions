class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        @cache
        def fun(i):
            if i==n-1:
                return cost[i]
            if i>=n:
                return 0
            c1 = cost[i]+fun(i+1)
            c2 = cost[i]+fun(i+2)
            return min(c1,c2)
        return min(fun(0),fun(1))
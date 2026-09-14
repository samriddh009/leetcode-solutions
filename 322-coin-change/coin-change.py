@cache
def fun(i,cur,target,coins):
    if cur == target:
        return 0
    if i>=len(coins) or cur>target:
        return float("inf")
    c1 = 1+fun(i,cur+coins[i],target,coins)
    c2 = fun(i+1,cur,target,coins)
    return min(c1,c2)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = fun(0,0,amount,tuple(coins))
        return ans if ans != float("inf") else -1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def fun(i,cur):
            if cur == amount:
                return 1
            if i>=len(coins) or cur>amount:
                return 0 
            c1 = fun(i,cur+coins[i])
            c2 = fun(i+1,cur)
            return c1+c2
        return fun(0,0)
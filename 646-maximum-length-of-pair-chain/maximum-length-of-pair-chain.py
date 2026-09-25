class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort()
        @cache
        def fun(i,pre):
            if i>=len(pairs):
                return 0
            c1 = fun(i+1,pre)
            c2 =0 
            if pairs[i][0]>pairs[pre][1] or pre==-1:
                c2 = 1+fun(i+1,i)
            return max(c1,c2)
        return fun(0,-1)
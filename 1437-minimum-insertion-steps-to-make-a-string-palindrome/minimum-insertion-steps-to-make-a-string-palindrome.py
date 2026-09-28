class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def fun(i,j):
            if i>j:
                return 0
            if s[i]==s[j]:
                return fun(i+1,j-1)
            else:
                c1 = 1+fun(i+1,j)
                c2 = 1+fun(i,j-1)
                return min(c1,c2)
        return fun(0,len(s)-1)
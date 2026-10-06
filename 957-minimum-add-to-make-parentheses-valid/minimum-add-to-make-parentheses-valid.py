class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        @cache
        def fun(i,c):
            if i == len(s):
                return c
            if s[i] == '(':
                return fun(i+1,c+1)
            if c > 0:
                return fun(i+1,c-1)
            return 1 + fun(i+1,c)
        return fun(0,0)
class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def f(i, bal):
            if bal < 0:
                return False
            if i == len(s):
                return bal == 0
            if s[i] == '(':
                return f(i + 1, bal + 1)
            if s[i] == ')':
                return f(i + 1, bal - 1)
            c1 = f(i + 1, bal + 1)   
            c2 = f(i + 1, bal - 1)   
            c3 = f(i + 1, bal)       
            return c1 or c2 or c3
        return f(0, 0)
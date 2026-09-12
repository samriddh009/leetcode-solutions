def check(i,j,s):
    if s[i]=='0':
        return False
    tmp = s[i:j+1]
    num = int(tmp, 2)
    for i in range(25):
        k = pow(5,i)
        if num == k:
            return True 
    return False
def fun(p,i,s):
    if i==len(s)-1:
        if check(p,i,s):
            return 0
        return 1000000000
    m = 1000000000
    if check(p,i,s):
        a = 1+fun(i+1,i+1,s)
        m = min(m,a)
    a = fun(p,i+1,s)
    m=min(m,a)
    return m
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        ans = fun(0,0,s)
        if ans == 1000000000:
            return -1
        return ans+1
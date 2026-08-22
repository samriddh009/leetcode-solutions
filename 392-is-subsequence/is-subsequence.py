def fun(i,j,s,t):
    if i>=len(s):
        return True 
    if j>=len(t):
        return False
    if s[i]==t[j]:
        return fun(i+1,j+1,s,t)
    else:
        return fun(i,j+1,s,t)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return fun(0,0,s,t)
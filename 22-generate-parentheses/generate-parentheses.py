def fun(s,oc,cc,n,ans):
    if oc>n or cc>n:
        return 
    if cc>oc:
        return 
    if oc+cc == 2*n:
        ans.append(s)
        return 
    fun(s+"(",oc+1,cc,n,ans)
    fun(s+")",oc,cc+1,n,ans)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        fun("",0,0,n,ans)
        return ans
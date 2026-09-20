class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,j in enumerate(s,1):
            ans+= i*(ord('z')-ord(j)+1)
        return ans
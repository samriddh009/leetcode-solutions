class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def fun(i,j):
            if i==len(s1):
                ans=0
                while j<len(s2):
                    ans+=ord(s2[j])
                    j+=1
                return ans
            if j==len(s2):
                ans = 0
                while i<len(s1):
                    ans+=ord(s1[i])
                    i+=1
                return ans
            if s1[i]==s2[j]:
                return fun(i+1,j+1)
            choice1 =ord(s1[i])+fun(i+1,j)
            choice2 = ord(s2[j])+fun(i,j+1)
            return min(choice1,choice2)
        return fun(0,0)
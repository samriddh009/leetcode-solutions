class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # text2 = text1[::-1]
        # @cache
        # def fun(i,j):
        #     if i>=len(text1) or j>=len(text2):
        #         return 0
        #     if text1[i]==text2[j]:
        #         return 1+fun(i+1,j+1)
        #     return max(fun(i+1,j),fun(i,j+1))
        # return fun(0,0)
        @cache 
        def fun(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return 2+fun(i+1,j-1)
            c2=fun(i+1,j)
            c3=fun(i,j-1)
            return max(c2,c3)
        return fun(0,len(s)-1)
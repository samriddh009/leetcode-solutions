class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def fun(i,j):
            if i>=len(word1):
                return len(word2)-j
            if j>=len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return fun(i+1,j+1)
            c1 = 1+fun(i+1,j)
            c2 = 1+fun(i+1,j+1)
            c3 = 1+fun(i,j+1)
            return min(c1,c2,c3)
        return fun(0,0)
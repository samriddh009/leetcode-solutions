class Solution:
    def maxDepth(self, s: str) -> int:
        max_c=0
        count =0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
                max_c =max(max_c,count)
            elif s[i]==')':
                count-=1
            else:
                continue
        return max_c
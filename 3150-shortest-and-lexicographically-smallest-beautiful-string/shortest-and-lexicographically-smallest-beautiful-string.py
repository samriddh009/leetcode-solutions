class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        res = float("inf")
        ones = 0
        low = 0
        for high in range(len(s)):
            if s[high] =='1':
                ones+=1
            while ones>k:
                if s[low] =='1':
                    ones-=1
                low+=1
            if ones==k:
                while s[low] == '0':
                    low+=1
                curr = s[low:high+1]
                if len(curr) < res or (len(curr) == res and curr < ans):
                    ans = curr
                    res = len(curr)
        return ans

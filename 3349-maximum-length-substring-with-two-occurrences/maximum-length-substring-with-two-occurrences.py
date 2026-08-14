from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        res = 0
        n = len(s)
        dit = defaultdict(int)
        for r in range(n):
            dit[s[r]] +=1
            while dit[s[r]]>2:
                dit[s[l]]-=1
                l +=1
            res = max(res, r - l + 1)
        return res
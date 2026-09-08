class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<=3:
            return 0
        return n-1000+1
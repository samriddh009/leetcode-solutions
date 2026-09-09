class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n))
        k = (l - 1) // 3
        if k == 0:
            return 0
        sum_p = (1000 * (10**(3 * k) - 1)) // 999
        return k * (n + 1) - sum_p
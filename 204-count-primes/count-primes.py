class Solution:
    def countPrimes(self, n: int) -> int:
        pr = [True] * n
        if n > 0:
            pr[0] = False
        if n > 1:
            pr[1] = False
        i = 2
        while i * i < n:
            if pr[i]:
                for j in range(i * i, n, i):
                    pr[j] = False
            i += 1
        return sum(pr)
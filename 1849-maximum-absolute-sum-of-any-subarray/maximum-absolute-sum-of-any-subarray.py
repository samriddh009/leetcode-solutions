class Solution:
    def maxAbsoluteSum(self, a: list[int]) -> int:
        best_max=a[0]
        best_min=a[0]
        res = abs(a[0])
        for i in range(1,len(a)):
            c1 = a[i]
            c2 = best_max+a[i]
            c3 = best_min+a[i]
            best_max =max(c1,c2)
            best_min = min(c1,c3)
            res = max(res,abs(best_max),abs(best_min))
        return res
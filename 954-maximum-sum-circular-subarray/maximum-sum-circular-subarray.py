class Solution:
    def maxSubarraySumCircular(self, a: list[int]) -> int:
        best_max = a[0]
        best_min = a[0]
        a1 = a[0]
        a2 =a[0]
        total = sum(a)
        for i in range(1,len(a)):
            c1 = a[i]
            c2 = a1+a[i]
            c3 = a2+a[i]
            a1 = max(c1,c2)
            a2 = min(c1,c3)
            best_max = max(best_max,a1)
            best_min = min(best_min,a2)
        if best_max<0:
            return best_max
        return max(best_max,total-best_min)
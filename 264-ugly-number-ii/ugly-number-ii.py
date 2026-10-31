class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            next_2 = ugly[p2] * 2
            next_3 = ugly[p3] * 3
            next_5 = ugly[p5] * 5
            
            next_val = min(next_2, next_3, next_5)
            ugly[i] = next_val
            
            if next_val == next_2:
                p2 += 1
            if next_val == next_3:
                p3 += 1
            if next_val == next_5:
                p5 += 1
                
        return ugly[-1]
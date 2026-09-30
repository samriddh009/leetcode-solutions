class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(i):
            sum1 = 0
            for j in range(len(piles)):
                sum1 += math.ceil(piles[j] / i)
            return sum1 <= h
        ans = max(piles)
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid   
                high = mid - 1
            else:
                low = mid + 1   
        return ans
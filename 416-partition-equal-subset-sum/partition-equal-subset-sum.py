from functools import cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
            
        target = total // 2
        n = len(nums)
        
        @cache
        def fun(i: int, rem: int) -> bool:
            if rem == 0:
                return True
            if i < 0 or rem < 0:
                return False
            return fun(i - 1, rem - nums[i]) or fun(i - 1, rem)
        return fun(n - 1, target)
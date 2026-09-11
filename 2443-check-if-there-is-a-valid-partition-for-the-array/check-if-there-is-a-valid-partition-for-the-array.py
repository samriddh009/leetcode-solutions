from functools import cache
from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True 
        def fun(i: int):
            if i >= n:
                return
            if i >= 1 and nums[i] == nums[i - 1] and dp[i - 1]:
                dp[i + 1] = True
            if i >= 2:
                if nums[i] == nums[i - 1] == nums[i - 2] and dp[i - 2]:
                    dp[i + 1] = True
                if nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and dp[i - 2]:
                    dp[i + 1] = True
            fun(i + 1)
        fun(0)
        return dp[n]
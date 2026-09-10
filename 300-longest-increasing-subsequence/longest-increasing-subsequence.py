class Solution:
    def __init__(self):
        self.dp = []
    def longest(self, nums, i, prev):
        if i >= len(nums):
            return 0
        if self.dp[prev + 1][i] != -1:
            return self.dp[prev + 1][i]
        notTake = self.longest(nums, i + 1, prev)
        take = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.longest(nums, i + 1, i)
        self.dp[prev + 1][i] = max(take, notTake)
        return self.dp[prev + 1][i]
    def lengthOfLIS(self, nums):
        n = len(nums)
        self.dp = [[-1] * n for _ in range(n + 1)]
        return self.longest(nums, 0, -1)
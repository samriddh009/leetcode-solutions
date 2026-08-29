def fun(i,nums,dp):
    if i>=len(nums):
        return 0
    if dp[i]!=-1:
        return dp[i]
    c1 = nums[i]+fun(i+2,nums,dp)
    c2 = fun(i+1,nums,dp)
    ans = max(c1,c2)
    dp[i] =ans
    return ans
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return fun(0,nums,dp)
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1]) 
        # for i in range(2,len(nums)):
        #     dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        # return dp[-1]
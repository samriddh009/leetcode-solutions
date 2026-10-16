# def fun(i,f,nums,n,dp):
#     if i>=n:
#         return 0
#     if i==n-1:
#         if f==0:
#             return nums[i]
#         return 0
#     if dp[i][f]!=-1:
#         return dp[i][f]
#     if i==0:
#         a=nums[i]+fun(i+2,1,nums,n,dp)
#         b=fun(i+1,f,nums,n,dp)
#     else:
#         a=nums[i]+fun(i+2,f,nums,n,dp)
#         b=fun(i+1,f,nums,n,dp)
#     dp[i][f]=max(a, b)
#     return dp[i][f]
class Solution:
    def rob(self, nums: List[int]) -> int:
        # n =len(nums)
        # dp= [[-1]*2 for _ in range(n+1)]
        # return fun(0,0,nums,n,dp)
        n = len(nums)
        if n==1:
            return nums[0]
        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for f in range(2):
                if i==n-1:
                    if f==0:
                        dp[i][f]=nums[i]
                    else:
                        dp[i][f]=0
                else:
                    if i==0:
                        a=nums[i]+dp[i+2][1]
                    else:
                        a=nums[i]+dp[i+2][f]
                    b=dp[i+1][f]
                    dp[i][f]=max(a,b)
        return dp[0][0]
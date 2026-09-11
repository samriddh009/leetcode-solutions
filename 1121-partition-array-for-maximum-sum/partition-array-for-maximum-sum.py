@cache
def fun(i,pre,nums,k):
    if i>=len(nums):
        return 0
    l = (i-pre+1)
    m = max(nums[pre:i+1])
    ans = 0
    if l==k:
        c1 = m*l+fun(i+1,i+1,nums,k)
        ans = max(ans,c1)
    else:
        c1 = m*l+fun(i+1,i+1,nums,k)
        c2 = fun(i+1,pre,nums,k)
        ans = max(ans,c1)
        ans = max(ans,c2)
    return ans
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return fun(0,0,tuple(arr),k)
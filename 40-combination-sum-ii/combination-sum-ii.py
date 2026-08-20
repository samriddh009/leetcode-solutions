def fun(nums,temp,ans,cur_sum,target):
    if cur_sum == target:
        ans.append(temp.copy())
        return
    if cur_sum > target or not nums:
        return
    for i in range(len(nums)):
        if i>0 and nums[i] ==nums[i-1] :
            continue
        ip = nums.copy()
        op = temp +[nums[i]]
        del ip[:i+1]
        fun(ip,op,ans,cur_sum+nums[i],target)
    return ans
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        fun(nums,[],ans,0,target)
        return ans
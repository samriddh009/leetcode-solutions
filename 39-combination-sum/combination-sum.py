#input output approach 
# def fun(nums,temp,cur_sum,ans,target,d):
#     if cur_sum == target:
#         k = tuple(sorted(temp))
#         if k not in d:
#             d[k]=1
#             ans.append(temp)
#         return 
#     if cur_sum>target:
#         return 
#     if not nums:
#         return 
#     for i in range(len(nums)):
#         op = temp +[nums[i]]
#         fun(nums,op,cur_sum+nums[i],ans,target,d)
#     return ans
#class Solution:
    #def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans = []
        # d = {}
        # fun(candidates,[],0,ans,target,d)
        # return ans

#take not take
def fun(i,nums,op,cur_sum,target,ans,d):
    if cur_sum == target:
        k = tuple(sorted(op))
        if k not in d:
            d[k]=1
            ans.append(op.copy())
        return 
    if cur_sum>target or i>=len(nums):
        return
    op.append(nums[i])
    fun(i, nums, op, cur_sum + nums[i], target, ans, d)
    op.pop()
    fun(i+1, nums, op, cur_sum, target, ans, d)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        d = {}
        fun(0,candidates,[],0,target,ans,d)
        return ans
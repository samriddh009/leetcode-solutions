#normal iteration approach
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = [[]]

        # for num in nums:
        #     new_subsets = []
        #     for curr in result:
        #         new_subsets.append(curr + [num])
        #     result.extend(new_subsets)

        # return result

#input output approach 
# def fun(nums,temp,ans):
#     ans.append(temp)
#     if not nums:
#         return 
#     for i in range(len(nums)):
#         ip = nums.copy()
#         op = temp +[nums[i]]
#         del ip[:i+1]
#         fun(ip,op,ans)
#     return ans

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
        #return fun(nums,[],[])

#take not take approach
def fun(i,nums,op,ans):
    if i>=len(nums):
        ans.append(op.copy())
        return 
    op.append(nums[i])
    fun(i+1,nums,op,ans)
    op.remove(nums[i])
    fun(i+1,nums,op,ans)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        fun(0,nums,[],ans)
        return ans
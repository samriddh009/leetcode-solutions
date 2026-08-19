def fun(nums,temp,ans):
    if not nums:
        ans.append(temp)
    for i in range(len(nums)):
        ip = nums.copy()
        op = temp +[nums[i]]
        del ip[i]
        fun(ip,op,ans)
    return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return fun(nums,[],[])
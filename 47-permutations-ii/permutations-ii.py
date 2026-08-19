def fun(nums,temp,ans):
    if not nums:
        ans.append(temp)
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            continue
        d[nums[i]] =1
        ip = nums.copy()
        op = temp+[nums[i]]
        del ip[i]
        fun(ip,op,ans)
    return ans

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return fun(nums,[],[])
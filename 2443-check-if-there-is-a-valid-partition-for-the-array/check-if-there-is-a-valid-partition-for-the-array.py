@cache
def fun(i,nums):
    n = len(nums)
    if i == n:
        return True
    if i + 2 <= n:
        if nums[i + 1] == nums[i]:
            if fun(i + 2,nums):
                return True
    if i + 3 <= n:
        if nums[i + 2] == nums[i + 1] and nums[i + 1] == nums[i]:
            if fun(i + 3,nums):
                return True
        if nums[i + 2] == nums[i + 1] + 1 and nums[i + 1] == nums[i] + 1:
            if fun(i + 3,nums):
                return True
    return False
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        return fun(0,tuple(nums))
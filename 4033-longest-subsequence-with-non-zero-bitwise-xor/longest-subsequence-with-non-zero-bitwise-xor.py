class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if 0 in set(nums) and len(set(nums))==1:
            return 0
        if len(nums)%2==0 and len(set(nums))==1:
            return len(nums)-1
        res = 0
        for i in range(len(nums)):
            res = res^nums[i]
        return len(nums) if res!=0 else len(nums)-1
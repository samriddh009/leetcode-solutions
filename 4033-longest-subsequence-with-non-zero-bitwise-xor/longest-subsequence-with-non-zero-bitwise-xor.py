class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res^nums[i]
        if res!=0:
            return len(nums)  
        if all(num == 0 for num in nums):
            return 0
        return len(nums)-1
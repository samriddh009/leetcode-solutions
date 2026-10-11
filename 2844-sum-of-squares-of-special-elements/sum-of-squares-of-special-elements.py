class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        for i in range(len(nums)):
            if n%(i+1)==0:
                c= nums[i]**2
                sum1+=c
        return sum1
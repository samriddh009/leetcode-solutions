class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        best = nums[0]
        second_best = nums[0]
        for i in range(1,len(nums)):
            c1 = best*nums[i]
            c2 = nums[i]
            c3 = second_best*nums[i]
            best = max(c1,c2,c3)
            second_best=min(c1,c2,c3)
            ans = max(ans,best,second_best)
        return ans
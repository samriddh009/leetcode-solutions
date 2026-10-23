class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, x in enumerate(nums):
            if i != x:
                k = k & x if k != -1 else x  # Or simply: k &= x
                
        return max(k, 0)
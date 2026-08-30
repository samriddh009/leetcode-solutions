class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums.index(min(nums))
        b = nums.index(max(nums))
        x, y = min(a, b), max(a, b)
        return min(y + 1,n - x,x + 1 + n - y)
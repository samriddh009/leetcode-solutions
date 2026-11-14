class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                size = j - i + 1
                if l <= size <= r and curr > 0:
                    ans = min(ans, curr)
        return -1 if ans == float('inf') else ans
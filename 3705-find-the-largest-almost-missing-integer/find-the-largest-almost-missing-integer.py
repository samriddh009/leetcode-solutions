class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = {}
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                d[x] = d.get(x, 0) + 1
        ans = -1
        for x in d:
            if d[x] == 1:
                ans = max(ans, x)
        return ans
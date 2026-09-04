class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            max_n = max(nums[:i+1])
            min_n = min(nums[i:len(nums)])
            print(max_n,min_n)
            if max_n-min_n<=k:
                return i
        return -1
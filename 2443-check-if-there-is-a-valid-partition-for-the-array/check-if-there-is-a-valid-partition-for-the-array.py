class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def fun(i):
            if i == n - 1:
                return True
            l = i + 2
            if l < n:
                if nums[l] == nums[l - 1]:
                    if fun(l):
                        return True
            l = i + 3
            if l < n:
                if nums[l] == nums[l - 1] and nums[l] == nums[l - 2]:
                    if fun(l):
                        return True
                if nums[l] == nums[l - 1] + 1 and nums[l - 1] == nums[l - 2] + 1:
                    if fun(l):
                        return True
            return False
        return fun(-1)
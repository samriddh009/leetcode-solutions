class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def fun(i: int) -> bool:
            if i == n - 1:
                return True
            next_2 = i + 2
            if next_2 < n:
                if nums[next_2] == nums[next_2 - 1]:
                    if fun(next_2):
                        return True
            next_3 = i + 3
            if next_3 < n:
                if nums[next_3] == nums[next_3 - 1] and nums[next_3] == nums[next_3 - 2]:
                    if fun(next_3):
                        return True
                if nums[next_3] == nums[next_3 - 1] + 1 and nums[next_3 - 1] == nums[next_3 - 2] + 1:
                    if fun(next_3):
                        return True
            return False
        if n >= 2 and nums[1] == nums[0]:
            if fun(1):
                return True
        if n >= 3:
            if nums[2] == nums[1] and nums[2] == nums[0]:
                if fun(2):
                    return True
            if nums[2] == nums[1] + 1 and nums[1] == nums[0] + 1:
                if fun(2):
                    return True
        return False
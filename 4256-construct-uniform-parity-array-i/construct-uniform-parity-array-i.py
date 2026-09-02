class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(nums1) == 1:
            return True

        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                for j in range(len(nums1)):
                    if i != j and nums1[j] % 2 == 1:
                        return True

        return True
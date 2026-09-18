class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        @cache
        def fun(i,j):
            if i>=len(nums1) or j>=len(nums2):
                return 0
            if nums1[i]==nums2[j]:
                return 1+fun(i+1,j+1)
            return max(fun(i+1,j),fun(i,j+1))
        return fun(0,0)
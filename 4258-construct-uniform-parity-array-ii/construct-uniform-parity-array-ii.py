class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        even = all(
            x % 2 == 0 or (x > mn and (x - mn) % 2 == 0)
            for x in nums1
        )
        odd = all(
            x % 2 == 1 or (x > mn and (x - mn) % 2 == 1)
            for x in nums1
        )
        return even or odd
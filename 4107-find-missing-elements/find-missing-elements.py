class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        j = 0

        for num in range(nums[0], nums[-1] + 1):
            if j < len(nums) and nums[j] == num:
                j += 1
            else:
                ans.append(num)

        return ans
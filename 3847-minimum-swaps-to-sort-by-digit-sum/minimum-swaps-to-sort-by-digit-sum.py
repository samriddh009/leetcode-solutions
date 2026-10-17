class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(arr)}
        a = nums[:]
        swaps = 0
        for i in range(len(a)):
            while pos[a[i]] != i:
                j = pos[a[i]]
                a[i], a[j] = a[j], a[i]
                swaps += 1
        return swaps
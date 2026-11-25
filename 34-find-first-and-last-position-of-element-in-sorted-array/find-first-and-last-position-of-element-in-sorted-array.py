class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        arr = []
        low, high = 0, len(nums)-1
        ans = len(nums)

        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        arr.append(ans)

        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ans = mid
                low = mid+1
            else:
                high = mid-1

        arr.append(ans)

        if arr[0] == len(nums) or arr[1] == -1:
            return [-1,-1]

        return arr
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        suffix = [0] * (n + 1)
        for k in range(1, n + 1):
            suffix[k] = suffix[k - 1] + nums[n - k]
        mini = float("inf")
        for i in range(n + 1):
            rem = x - prefix[i]
            if rem < 0:
                break
            low, high = 0, n - i
            while low <= high:
                mid = (low + high) // 2
                if suffix[mid] == rem:
                    mini = min(mini, i + mid)
                    break
                elif suffix[mid] < rem:
                    low = mid + 1
                else:
                    high = mid - 1
        return mini if mini != float("inf") else -1
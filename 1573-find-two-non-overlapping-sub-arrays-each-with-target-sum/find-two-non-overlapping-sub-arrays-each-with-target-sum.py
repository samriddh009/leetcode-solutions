class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        low = 0
        curr = 0
        res = []
        for high in range(len(arr)):
            curr += arr[high]
            while curr > target:
                curr -= arr[low]
                low += 1
            if curr == target:
                res.append([low, high])
        if len(res) < 2:
            return -1
        res.sort()
        n = len(res)
        v = [0] * n
        for i in range(n):
            v[i] = res[i][1] - res[i][0] + 1
        dp = [10**9] * n
        dp[0] = v[0]                 
        ans = 10**9
        j = 0
        for i in range(1, n):
            dp[i] = min(dp[i - 1], v[i]) 
            while j < i and res[j][1] < res[i][0]:
                j += 1
            if j > 0:
                ans = min(ans, dp[j - 1] + v[i])
        return -1 if ans == 10**9 else ans
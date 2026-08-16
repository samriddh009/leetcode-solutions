class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ans = [-1]*len(arrivalTime)
        max_l = max(lights)
        for i in range(len(arrivalTime)):
            r = arrivalTime[i]%period
            if r<max_l:
                ans[i] = 0
            else:
                ans[i] = period-r
        return max(ans)
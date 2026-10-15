class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        activities = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in activities]
        n = len(activities)
        memo = {}
        
        def binary_search(target):
            low = 0
            high = n - 1
            ans = n
            while low <= high:
                mid = (low + high) // 2
                if starts[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def fun(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            exclude = fun(i + 1)
            next_idx = binary_search(activities[i][1])
            include = activities[i][2] + fun(next_idx)
            
            memo[i] = max(exclude, include)
            return memo[i]

        return fun(0)
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        pre = [0]*n
        pre[0] = tasks[0]
        for i in range(1,n):
            pre[i] = pre[i-1]+tasks[i]
        ans = []
        i = 0
        do = pre[-1]
        for t in shifts:
            i +=t
            if i>=do:
                ans.append(0)
                i = 0
                continue
            low = 0
            high = n-1
            while low<=high:
                mid = (low+high)//2
                if pre[mid]<=i:
                    low = mid+1
                else:
                    high= mid-1
            ans.append(n-low)
        return ans
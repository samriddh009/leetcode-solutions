class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        res = arr[0]
        nodel = arr[0]
        onedel = float("-inf")
        for i in range(1,len(arr)):
            pre_no = nodel
            pre_one = onedel
            c1 = arr[i]
            c2 = pre_no+arr[i]
            nodel=max(c1,c2)
            v2 = 0
            if pre_one==float("-inf"):
                v2 = arr[i]
            else:
                v2 = pre_one+arr[i]
            c3 = pre_no
            onedel = max(v2,c3)
            res = max(res,onedel,nodel)
        return res
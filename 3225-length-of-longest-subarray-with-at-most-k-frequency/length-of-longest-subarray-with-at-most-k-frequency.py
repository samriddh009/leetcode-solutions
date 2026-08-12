class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("-inf")
        low =0
        d = defaultdict(int)
        for high in range(len(nums)):
            d[nums[high]] +=1
            while d[nums[high]]>k:
                d[nums[low]]-=1
                if d[nums[low]]==0:
                    del d[nums[low]]
                low+=1
            length = high-low+1
            res = max(res,length)
        return res
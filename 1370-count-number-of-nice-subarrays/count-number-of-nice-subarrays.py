class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        low = 0
        odd = 0
        even = 0
        n = len(nums)
        for high in range(0,n):
            if nums[high]%2!=0:
                odd +=1
                even = 0
            while odd>k:
                if nums[low]%2!=0:
                    odd-=1
                low+=1
            if odd==k:
                while nums[low]%2==0:
                    even +=1
                    low+=1
                count += even+1
        return count

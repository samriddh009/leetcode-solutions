class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        if sum(diff) <= k:
            return 0
        
        m = max(diff)
        cnt = [0] * (m + 1)
        for d in diff:
            cnt[d] += 1
            
        for d in range(m, 0, -1):
            if cnt[d] == 0:
                continue
            
            if k >= cnt[d]:
                k -= cnt[d]
                cnt[d - 1] += cnt[d]
                cnt[d] = 0
            else:
                cnt[d - 1] += k
                cnt[d] -= k
                k = 0
                break
                
        return sum(c * (d * d) for d, c in enumerate(cnt))
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        ans = 0
        while left <= n - k:
            matched = False
            for length in (k, k + 1):
                right = left + length
                if right <= n:
                    window = s[left:right]
                    if window == window[::-1]:
                        ans += 1
                        left = right   
                        matched = True
                        break
            if not matched:
                left += 1
        return ans
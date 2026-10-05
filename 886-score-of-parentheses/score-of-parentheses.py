class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def solve(l, r):
            if r - l == 1:     
                return 1
            count = 0
            for i in range(l, r + 1):
                if s[i] == '(':
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    if i == r:
                        return 2 * solve(l + 1, r - 1)
                    else:
                        return solve(l, i) + solve(i + 1, r)
        return solve(0, len(s) - 1)
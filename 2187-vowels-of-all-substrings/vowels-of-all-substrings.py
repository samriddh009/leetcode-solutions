class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * n

        def solve(i):
            if i == n:
                return 0

            if i == 0:
                dp[i] = 1 if word[i] in "aeiou" else 0
            else:
                dp[i] = dp[i - 1]

                if word[i] in "aeiou":
                    dp[i] += i + 1

            return dp[i] + solve(i + 1)

        return solve(0)
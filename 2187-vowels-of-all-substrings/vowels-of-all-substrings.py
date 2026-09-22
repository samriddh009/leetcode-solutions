class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * n
        def fun(i):
            if i == n:
                return 0
            if i == 0:
                if word[i] in "aeiou":
                    dp[i] = 1  
                else:
                    dp[i] = 0
            else:
                dp[i] = dp[i - 1]
                if word[i] in "aeiou":
                    dp[i] += i + 1
            return dp[i] + fun(i + 1)
        return fun(0)
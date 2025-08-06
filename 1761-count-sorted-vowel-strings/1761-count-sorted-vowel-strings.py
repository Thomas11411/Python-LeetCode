class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for i in range(1,n):
            for j in range(5):
                dp[j] = sum(dp[j:])

        return sum(dp)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = []
        for l in range(n):
            for i in range(n-l):
                j = i + l
                if l == 0:
                    dp[i][j] = 1
                    res = s[i]   
                    continue

                if s[i] == s[j]:
                    if l <= 2:
                        dp[i][j] = 1
                        res = s[i:j+1]   
                    else:
                        if dp[i+1][j-1] == 1:
                            dp[i][j] = 1
                            res = s[i:j+1]     
        return res
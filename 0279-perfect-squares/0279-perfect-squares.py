class Solution:
    def numSquares(self, n: int) -> int:

        dp = [0]
        while len(dp) < n + 1:
            m = len(dp)
            dp.append(min([dp[m - j*j] for j in range(1,int(m ** 0.5) + 1 )]) + 1)

        return dp[-1]
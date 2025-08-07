class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        from collections import defaultdict

        d = defaultdict(int)

        for i,v in enumerate(map(chr, range(ord('a'), ord('z')+1))):
            d[v] = i

        dp = [0] * 26
        res = 0

        for i in s:

            dp[d[i]] = max(dp[max(d[i]-k,0):min(d[i]+k,25)+1]) + 1
            res = max(res,dp[d[i]])

        return res
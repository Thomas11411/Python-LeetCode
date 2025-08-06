class Solution:
    def beautySum(self, s: str) -> int:
        if len(s) <= 2:
            return 0

        from collections import defaultdict

        res = 0

        for i in range(0,len(s)-2):
            d = defaultdict(int)
            for j in range(i,len(s)):
                d[s[j]] += 1
                res += (max(d.values()) - min(d.values()))

        return res
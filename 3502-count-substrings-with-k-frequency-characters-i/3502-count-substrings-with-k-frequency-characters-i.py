class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        from collections import defaultdict
        n = len(s)
        res = (n + 1) * n // 2
        i = 0
        d = defaultdict(int)

        for j in range(n):
            d[s[j]] += 1
            
            while d[s[j]] == k:
                d[s[i]] -= 1
                i += 1
            
            res -= (j - i + 1)

        return res
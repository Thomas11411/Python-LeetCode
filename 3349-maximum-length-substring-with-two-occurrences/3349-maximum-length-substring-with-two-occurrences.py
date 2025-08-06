class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
                
        from collections import defaultdict

        d = defaultdict(int)
        i = 0
        res = 0

        for j in range(len(s)):
            d[s[j]] += 1
            
            while d[s[j]] > 2:
                d[s[i]] -= 1
                i += 1
                
            res = max(res, j - i + 1)

        return res
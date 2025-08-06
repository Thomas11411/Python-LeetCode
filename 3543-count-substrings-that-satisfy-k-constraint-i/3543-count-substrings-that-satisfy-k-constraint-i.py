class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        from collections import defaultdict

        d = defaultdict(int)
        i = 0
        res = 0

        for j in range(len(s)):
            d[s[j]] += 1
            
            while d["1"] > k and d["0"] > k:
                d[s[i]] -= 1
                i += 1
                
            res += (j - i + 1)

        return res
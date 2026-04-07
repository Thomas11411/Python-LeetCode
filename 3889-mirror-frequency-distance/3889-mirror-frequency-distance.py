class Solution:
    def mirrorFrequency(self, s: str) -> int:
        from collections import Counter

        d = Counter(s)
        res = 0

        for i in range(13):
            res += abs(d[string.ascii_lowercase[i]] - d[string.ascii_lowercase[~i]])
            
        for i in range(5):
            res += abs(d[string.digits[i]] - d[string.digits[~i]])

        return res
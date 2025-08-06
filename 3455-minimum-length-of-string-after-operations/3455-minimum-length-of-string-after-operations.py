class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter

        d = Counter(s)
        res = 0

        for i in set(s):
            res += (2 if d[i] % 2 == 0 else 1)

        return res
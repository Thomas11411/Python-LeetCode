class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        from collections import Counter

        d = Counter(str(n))
        return int(min(d, key = lambda x: (d[x], x)))

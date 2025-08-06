class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        from collections import Counter

        d = Counter(i % 24 for i in hours)

        return int(sum((d[i] * d[24-i]) for i in range(1, 12)) + d[0] * (d[0] - 1) / 2 + d[12] * (d[12] - 1) / 2)
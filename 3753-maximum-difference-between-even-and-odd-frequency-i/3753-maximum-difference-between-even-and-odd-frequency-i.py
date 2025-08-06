class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter

        cnt = Counter(s).values()

        return max(v for v in cnt if v % 2 == 1) - min(v for v in cnt if v % 2 == 0)
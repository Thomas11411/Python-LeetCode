class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter

        d = Counter(s)

        return sum(sorted(list(d.values()))[:(len(d) - k)]) if len(d) > k else 0
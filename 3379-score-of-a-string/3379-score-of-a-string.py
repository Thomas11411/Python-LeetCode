class Solution:
    def scoreOfString(self, s: str) -> int:

        import itertools

        return sum(abs(ord(i) - ord(j)) for i, j in itertools.pairwise(s))
        
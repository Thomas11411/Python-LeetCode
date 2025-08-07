class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        from collections import Counter

        d = Counter(s)

        return int(100 * d[letter] / len(s))
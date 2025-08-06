class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import defaultdict

        res = 0
        word = set(word)
        d = defaultdict(int)

        for i in word:
            d[i.lower()] += 1

        return sum(i == 2 for i in d.values())
        
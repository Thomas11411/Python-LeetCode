class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        word1_c = Counter(word1)
        word2_c = Counter(word2)

        for i in list(word2_c.keys()) + list(word1_c.keys()):
            if abs(word1_c[i] - word2_c[i]) > 3:
                return False
        return True
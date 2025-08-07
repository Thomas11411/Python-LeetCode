class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        cwords1 = Counter(words1)
        cwords2 = Counter(words2)
        return sum(1 for i in cwords1.keys() if cwords1[i] == cwords2[i] == 1)
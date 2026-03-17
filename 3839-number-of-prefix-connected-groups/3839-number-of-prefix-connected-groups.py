class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        from collections import Counter

        d = Counter()
        res = 0

        for word in words:
            
            if len(word) < k: continue
            d[word[:k]] += 1
            
            if d[word[:k]] == 2: res += 1
        return res
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        from collections import Counter
        import math

        d = Counter()

        for i in s:
            if i.isalpha():
                if i in {"a", "e", "i", "o", "u"}:
                    d["v"] += 1
                else:
                    d["c"] += 1
                    
        return math.floor(d["v"] / d["c"]) if d["c"] > 0 else 0
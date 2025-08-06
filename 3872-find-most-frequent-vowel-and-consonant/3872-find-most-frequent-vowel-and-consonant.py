class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        v = 0
        c = 0
        d = Counter()

        for i in s:
            
            d[i] += 1
            
            if i in "aeiou":
                v = max(v, d[i])
            else:
                c = max(c, d[i])
                
        return v + c
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        a = 0
        v = 0

        for i in s:
            a += i.isalpha()
            v += (i in {"a","e","i","o","u"})
                    
        return math.floor(v / (a - v)) if a - v > 0 else 0
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
                
        from collections import Counter

        d = Counter(s)
        mx = max(d.values())

        res = ""

        for i in reversed(s):
            if d[i] == mx and i not in res:
                res += i
                
        return res[::-1]
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        from collections import Counter

        t = map(lambda x: int(x), t)
        s = map(lambda x: int(x), s)

        dt = Counter(t)
        res = ""

        for i,v in enumerate(s):
            if dt[v ^ 1] > 0: 
                res += "1"
                dt[v ^ 1] -= 1
            else:
                res += "0"
                dt[v] -= 1
        return res
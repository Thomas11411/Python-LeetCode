class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        from collections import Counter

        dt = Counter(list(t))
        res = ""

        for i,v in enumerate(s):
            if dt[str(int(v) ^ 1)] > 0: 
                res += "1"
                dt[str(int(v) ^ 1)] -= 1
            else:
                res += "0"
                dt[v] -= 1
        return res
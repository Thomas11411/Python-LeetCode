class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        from collections import defaultdict

        d = defaultdict(lambda: float("-inf"))
        res = ""
        cnt = 0

        for i,v in enumerate(s):
            if d[v] + k >= cnt: continue
            d[v] = cnt
            res += v
            cnt += 1
        return res
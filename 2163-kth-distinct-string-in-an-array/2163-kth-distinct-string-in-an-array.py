class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import defaultdict
        d = defaultdict(int)
        res = []
        for i in arr:
            d[i] += 1
            if d[i] == 1:
                res.append(i)
            elif d[i] == 2:
                res.remove(i)
        return res[k - 1] if k <= len(res) else ""
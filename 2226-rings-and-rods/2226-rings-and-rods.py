class Solution:
    def countPoints(self, rings: str) -> int:
        from collections import defaultdict
        d = defaultdict(set)
        res = set()

        for i in range(len(rings) // 2):
            d[rings[int(i * 2 + 1)]].add(rings[int(i * 2)])
            if len(d[rings[int(i * 2 + 1)]]) == 3:
                res.add(rings[int(i * 2 + 1)])

        return len(res)
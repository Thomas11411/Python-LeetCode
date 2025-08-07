class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        from collections import defaultdict

        d = defaultdict(list)

        res = float('inf')
        for i,v in enumerate(cards):
            if d[v]:
                res = min(res,i - d[v][-1] + 1)
            d[v].append(i)

        return res if res != float("inf") else -1
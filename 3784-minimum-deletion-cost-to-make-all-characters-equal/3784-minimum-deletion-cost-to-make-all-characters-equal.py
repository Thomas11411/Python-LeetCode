class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        from collections import defaultdict

        d = defaultdict(int)

        for i, v in zip(s, cost):
            d[i] += v
            
        return sum(cost) - max(d.values())
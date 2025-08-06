class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        from collections import defaultdict

        d = defaultdict(int)
        for i, j in zip(x, y):
            d[i] = max(d[i], j)
            
        res = sorted(d.values(), reverse = True)
        return sum(res[0:3]) if len(res) >= 3 else -1
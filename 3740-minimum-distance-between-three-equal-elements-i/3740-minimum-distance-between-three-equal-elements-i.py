class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict

        d = defaultdict(list)
        res = float('inf')

        for i, v in enumerate(nums):
            d[v].append(i)
            if len(d[v]) < 3: continue
            res = min(res, 2 * (d[v][-1] - d[v][-3]))

        return res if res != float('inf') else -1
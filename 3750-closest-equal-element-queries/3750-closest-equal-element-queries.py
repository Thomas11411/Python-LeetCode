class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        import bisect

        d = defaultdict(list)
        res = []
        n = len(nums)

        for i,v in enumerate(nums): 
            d[v].append(i)

        for q in queries:
            idx = d[nums[q]]
            m = len(idx)
            if len(idx) == 1: 
                res.append(-1)
                continue
            
            j = bisect.bisect_left(idx, q)
            res.append(min(abs(q - idx[j - 1]), n - abs(q - idx[j - 1]), abs(q - idx[(j + 1) % m]), n - abs(q - idx[(j + 1) % m])))

        return res
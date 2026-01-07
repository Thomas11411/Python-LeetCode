class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from heapq import heappushpop

        d = [[0] * 3 for _ in range(3)]

        for n in nums:
            heappushpop(d[n % 3], n)
            
        tri = [max(h) for h in d]

        if 0 in tri: res = 0
        else: res = sum(tri)

        for h in d:
            if 0 in h: continue
            else: res = max(res, sum(h))
        return res
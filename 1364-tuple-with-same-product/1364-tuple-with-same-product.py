class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        import itertools
        from collections import defaultdict
        res = 0
        d1 = defaultdict(int)
        for x,y in itertools.combinations(nums,2): 
            d1[x * y] += 1
            if d1[x * y] > 1:
                res += (d1[x * y] - 1) * 8
        return res
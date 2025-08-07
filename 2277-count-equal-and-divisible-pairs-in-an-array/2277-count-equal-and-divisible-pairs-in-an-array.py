class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        d = defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)

        res = 0
        for idx, val in d.items():
            l = len(val)
            for i in range(0,l-1):
                for j in range(i+1,l):
                    if (val[i] * val[j]) % k == 0:
                        res += 1

        return res
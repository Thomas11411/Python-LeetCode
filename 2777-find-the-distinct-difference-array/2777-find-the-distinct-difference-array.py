class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        import collections

        l = collections.defaultdict(int)
        r = collections.Counter(nums)
        cur = - len(r)
        res = []

        for i in nums:
            r[i] -= 1
            l[i] += 1
            cur += (l[i] == 1) + (r[i] == 0) 
            res.append(cur)

        return res
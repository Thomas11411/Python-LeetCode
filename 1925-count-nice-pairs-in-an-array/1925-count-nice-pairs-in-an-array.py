class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        res = 0

        for i in nums:
            temp = i - int(str(i)[::-1])
            d[temp] += 1

            if d[temp] > 1:
                res += d[temp] - 1

        return res % (10**9+7)
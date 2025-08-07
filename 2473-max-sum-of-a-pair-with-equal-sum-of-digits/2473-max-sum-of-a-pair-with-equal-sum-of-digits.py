class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict

        nums.sort()

        def divide(x,y):
            if x // 10 == 0:
                return y + x
            y += (x % 10)
            return divide(x // 10,y)

        d = defaultdict(list)

        res = -1

        for i in nums:
            now = divide(i,0)
            d[now].append(i)

            if len(d[now]) >= 2:
                res = max(res,d[now][-1]+d[now][-2])

        return res
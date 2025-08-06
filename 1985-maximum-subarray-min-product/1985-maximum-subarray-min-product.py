class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        import itertools
        stack = []
        res = 0
        acc = [0] + list(itertools.accumulate(nums))

        for i,v in enumerate(nums + [0]):
            j = i
            while stack and stack[-1][1] > v:
                j , low = stack.pop()
                res = max(res,( acc[i] - acc[j] ) * low )

            stack.append([j,v])

        return res % (10**9 + 7)
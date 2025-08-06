class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        from itertools import accumulate

        acc = list(accumulate(nums, initial = 0))
        mn = float('inf')
        n = len(nums)
        test = []

        for i in range(n):
            for d in range(l, r + 1):
                j = i + d
                if j > n: continue
                if acc[j] - acc[i] > 0: mn = min(mn, acc[j] - acc[i])

        return -1 if mn == float('inf') else mn
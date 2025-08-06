class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        sum_ = sum(nums)
        rounds = target // sum_
        target %= sum_

        res = float('inf')
        cur = 0
        d = {0: -1}

        for i in range(len(nums) * 2):
            cur += nums[i % len(nums)]
            d[cur] = i
            if cur - target in d:
                res = min(res, i - d[cur - target])
                
        res += rounds * len(nums)

        return res if res != float('inf') else -1
        
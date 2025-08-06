class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
                
        from collections import defaultdict

        n = len(nums)
        d = defaultdict(int)
        res = 0
        i = 0

        for j in range(n):
            d[nums[j]] += 1
            while d[nums[j]] > k:
                d[nums[i]] -= 1
                i += 1
                
            res = max(res, j - i + 1)

        return res
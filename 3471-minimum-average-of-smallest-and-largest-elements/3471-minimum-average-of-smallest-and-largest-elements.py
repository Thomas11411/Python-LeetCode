class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        res = float('inf')

        for i in range(n):
            res = min(res, (nums[i] + nums[n - i - 1]) / 2)

        return res
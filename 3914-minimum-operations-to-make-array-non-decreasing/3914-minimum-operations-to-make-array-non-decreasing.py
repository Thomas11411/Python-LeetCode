class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(1, n):
            res += max(0, nums[i - 1] - nums[i])
        return res
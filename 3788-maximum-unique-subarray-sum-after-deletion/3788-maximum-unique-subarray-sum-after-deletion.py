class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos = set([i for i in nums if i > 0])
        return sum(pos) if len(pos) > 0 else max(nums)
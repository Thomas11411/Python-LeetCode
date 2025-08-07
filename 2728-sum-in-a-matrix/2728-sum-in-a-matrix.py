class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        return sum(max(c) for c in zip(*[sorted(r) for r in nums]))
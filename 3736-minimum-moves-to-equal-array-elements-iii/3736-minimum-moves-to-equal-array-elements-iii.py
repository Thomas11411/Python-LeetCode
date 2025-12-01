class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(map(lambda x: max(nums) - x, nums))
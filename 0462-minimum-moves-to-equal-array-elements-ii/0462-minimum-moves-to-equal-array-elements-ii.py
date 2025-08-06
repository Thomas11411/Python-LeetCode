class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) >> 1]
        
        return sum([abs(i - mid) for i in nums])
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return 2 * sum(i for i in nums if i < 10) != sum(nums)
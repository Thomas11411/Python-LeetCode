class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        from numpy import mean

        start = int(mean(nums)) + 1
        start = start if start > 1 else 1 

        for i in range(start, 102):
            if i not in nums: return i
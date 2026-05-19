class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        nums = list(map(int, s))

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 2: return False
        return True
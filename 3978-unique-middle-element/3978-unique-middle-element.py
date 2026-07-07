class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        from collections import Counter

        d = Counter(nums)
        return d[nums[len(nums) // 2]] == 1
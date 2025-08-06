class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter

        d = Counter(nums)
        m = max(d.values())

        return m * sum(i == m for i in d.values())
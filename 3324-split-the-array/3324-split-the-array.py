class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter

        d = Counter(nums)

        return all(i <= 2 for i in d.values())
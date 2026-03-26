class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        from collections import Counter

        d1 = Counter(nums)
        d2 = Counter(d1.values())

        for num in nums:
            if d2[d1[num]] == 1: return num
        return -1
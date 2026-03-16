class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        from collections import Counter

        d = Counter(nums)

        for i in nums:
            if d[i] == 1 and i % 2 == 0:
                return i
        return -1
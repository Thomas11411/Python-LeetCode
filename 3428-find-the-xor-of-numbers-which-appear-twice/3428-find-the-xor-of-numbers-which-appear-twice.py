class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        from collections import Counter

        d = Counter(nums)
        res = 0

        for i in d.keys():
            if d[i] == 2:
                res ^= i

        return res
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter

        d = Counter(nums)

        res = []

        for i, v in d.items():
            v = min(v, k)
            res += [i] * v
        return res
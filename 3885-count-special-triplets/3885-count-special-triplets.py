class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        l = Counter()
        r = Counter(nums)
        res = 0

        for i in nums:
            r[i] -= 1
            res += (r[i * 2] * l[i * 2])
            l[i] += 1

        return res % (10 ** 9 + 7)
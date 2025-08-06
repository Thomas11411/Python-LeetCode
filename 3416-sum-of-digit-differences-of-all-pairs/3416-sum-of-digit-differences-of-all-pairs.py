class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(str(nums[0]))
        res = m * (n * (n - 1) // 2)
        cnt = [[0] * 10 for i in range(m)]

        for s in nums:
            for i, v in enumerate(str(s)):
                res -= cnt[i][int(v)]
                cnt[i][int(v)] += 1

        return res
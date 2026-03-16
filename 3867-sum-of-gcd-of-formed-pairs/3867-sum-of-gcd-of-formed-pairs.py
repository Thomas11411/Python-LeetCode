class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        from math import gcd

        new = []
        mx, res, n = 0, 0, len(nums) // 2

        for num in nums:
            if num > mx: mx = num
            new.append(gcd(mx, num))

        new.sort()

        for i in range(n):
            res += gcd(new[i], new[~i])
        return res
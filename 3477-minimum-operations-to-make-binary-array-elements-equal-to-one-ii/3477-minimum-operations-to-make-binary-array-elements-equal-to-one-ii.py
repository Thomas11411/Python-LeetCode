class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter

        n = len(nums)

        d = Counter(nums)

        res = 0

        for i in range(n):
            if abs(nums[i] - (res % 2)) == 0:
                zero = d[0]
                one = d[1]
                d[0] = one
                d[1] = zero - 1
                res += 1
            else:
                d[1] -= 1

        return res
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)

        for i in range(n // 2):
            res += int(str(nums[i]) + str(nums[n - i - 1]))

        if n % 2 == 1:
            res += nums[(n // 2)]

        return res
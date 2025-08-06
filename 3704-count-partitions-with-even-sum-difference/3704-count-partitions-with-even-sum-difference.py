class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        res = 0

        for i in range(len(nums) - 1):
            right -= i
            left += i
            res += ((right - left) % 2 == 0)

        return res
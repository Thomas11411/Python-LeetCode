class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            test = 2
            if (i - k) >= 0 and nums[i] <= nums[i - k]: test -= 1
            if (i + k) <= (n - 1) and nums[i] <= nums[i + k]: test -= 1
            
            if test == 2: res += nums[i]

        return res
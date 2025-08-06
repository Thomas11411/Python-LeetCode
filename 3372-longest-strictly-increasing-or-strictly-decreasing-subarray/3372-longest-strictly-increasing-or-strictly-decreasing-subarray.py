class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
                
        de = 1
        cr = 1

        res = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cr += 1
                de = 1
            elif nums[i] < nums[i - 1]:
                cr = 1
                de += 1
            else:
                cr = 1
                de = 1
                
            res = max(res, cr, de)

        return res
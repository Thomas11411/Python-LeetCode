class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res , now = nums[0] , nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                now += nums[i]
            else:
                now = nums[i]
            res = max(res , now)
        return res
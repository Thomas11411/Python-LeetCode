class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start , end  = 0 , k
        nums_sum = sum(nums[:k])
        nums_avg = nums_sum / k
        while end < len(nums):
            nums_sum = nums_sum - nums[start] + nums[end]
            nums_avg = max( nums_avg, nums_sum / k )
            start += 1
            end += 1
        return nums_avg
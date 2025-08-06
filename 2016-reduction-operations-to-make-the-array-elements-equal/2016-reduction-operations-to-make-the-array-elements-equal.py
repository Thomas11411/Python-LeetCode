class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        now , res = 0 , 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] : now += 1
            res += now
        return res
class Solution:
    def minOperations(self, nums: List[int]) -> int:
                
        n = len(nums)

        res = 0

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                res += 1
                
        return res if (nums[-1] == 1 and nums[-2] == 1) else -1
class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        dp = [False] * (len(nums) + 1)

        dp[0] = True

        for i in range(2,len(nums) + 1):
            if nums[i - 2] == nums[i - 1]:
                dp[i] = dp[i] or dp[i - 2]
                
            if i < 3:
                continue
                
            if nums[i - 3] == nums[i - 2] == nums[i - 1]:
                dp[i] = dp[i] or dp[i - 3]
                
            if nums[i - 3] + 1 == nums[i - 2] == nums[i - 1] - 1:
                dp[i] = dp[i] or dp[i - 3]
            
            
        return dp[-1]
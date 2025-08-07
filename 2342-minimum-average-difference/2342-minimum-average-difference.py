class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l , r , n = 0 , sum(nums) , len(nums)
        cnt = float('inf')
        res = 0

        for i in range(0,n - 1):
            l += nums[i]
            r -= nums[i]
            now = abs((l // (i + 1)) - (r // (n - i - 1)))
            if cnt > now:
                cnt = now
                res = i
        
        if cnt > sum(nums) // n:
            res = n - 1

        return res
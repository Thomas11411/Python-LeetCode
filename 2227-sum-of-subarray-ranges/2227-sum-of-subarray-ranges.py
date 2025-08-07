class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 1):
            mx , mn = nums[i] , nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] > mx:
                    mx = nums[j]
                if nums[j] < mn:
                    mn = nums[j]
                res += (mx - mn)

        return res
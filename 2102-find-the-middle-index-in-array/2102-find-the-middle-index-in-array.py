class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l , r = 0 , sum(nums[1:])
        if l == r:
            return 0
        for i in range(1,len(nums)):
            l += nums[i - 1]
            r -= nums[i]
            if l == r:
                return i
        return -1
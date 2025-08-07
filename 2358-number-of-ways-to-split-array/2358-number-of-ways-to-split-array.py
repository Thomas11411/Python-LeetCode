class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        i , l , r , res = 0 , 0 ,sum(nums) , 0

        while i < len(nums) - 1:
            l += nums[i]
            r -= nums[i]
            if l >= r:
                res += 1
            i += 1

        return res
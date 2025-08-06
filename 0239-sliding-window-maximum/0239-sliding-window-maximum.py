class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res =[]        
        l =0 
        
        if len(nums) ==0:
            return []
        if len(nums)<k:
            return max(nums)
        
        while l< len(nums)-k+1:
            res.append(max(nums[l:l+k]))
            l+= 1
        return res
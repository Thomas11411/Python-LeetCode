class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))
        return min(max(idx1,idx2)+1,max(len(nums)-idx1,len(nums)-idx2),min(idx1,idx2)+1+len(nums)-max(idx1,idx2))
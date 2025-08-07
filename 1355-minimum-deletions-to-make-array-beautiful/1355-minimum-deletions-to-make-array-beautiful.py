class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        l , n , res = 0 , len(nums) , 0

        while l < n - 1:
            if nums[l] == nums[l + 1]:
                l += 1
                res += 1
            else:
                l += 2

        return res + (n - res) % 2
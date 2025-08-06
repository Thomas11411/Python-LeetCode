class Solution:
    def isGood(self, nums: List[int]) -> bool:

        nums.sort()

        n = len(nums)

        for i in range(n - 1):
            if (i + 1) != nums[i]:
                return False
            
        return True if nums[n - 1] == (n - 1) else False
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        tmp = set()

        for i in range(1,len(nums)):
            if nums[i] + nums[i - 1] in tmp:
                return True
            tmp.add(nums[i] + nums[i - 1])
        return False
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        j = len(nums) - 1
        res = 0
        for i in range((n // 2)-1, -1, -1):
            if nums[i] * 2 <= nums[j]:
                res += 2
                j -= 1

        return res
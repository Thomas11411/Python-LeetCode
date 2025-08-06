class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(1,n):
            if nums[i - 1] > nums[i]:
                tmp = nums[i:] + nums[:i]
                return n - i if tmp == sorted(nums) else -1

        return 0

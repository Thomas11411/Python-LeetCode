class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        lo = 0
        hi = len(nums) - 1
        res = 0

        while hi > lo:
            if nums[hi] + nums[lo] < target:
                res += (hi - lo)
                lo += 1
            else:
                hi -= 1

        return res
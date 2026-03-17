class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        cnt = len(nums) - 1
        sum_ = sum(nums)
        res = 0

        for i in range(len(nums) - 1):
            sum_ -= nums[i]
            res += (nums[i] > (sum_ / cnt))
            cnt -= 1

        return res
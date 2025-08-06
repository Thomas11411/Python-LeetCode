class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        for i in range(int(len(nums) / 2)):
            res.append(nums[i] + nums[len(nums) - i - 1])
        return max(res)
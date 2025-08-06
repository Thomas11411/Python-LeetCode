class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        res = 0

        for i in range(1, len(nums), 2):
            if nums[i] + nums[i - 1] == score: res += 1
            else: return res

        return res
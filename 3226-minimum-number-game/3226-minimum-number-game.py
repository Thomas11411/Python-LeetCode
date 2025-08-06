class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            a = max(nums[i], nums[i + 1])
            b = min(nums[i], nums[i + 1])
            res += [a,b]

        return res
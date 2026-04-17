class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sum2 = [i * i for i in nums]
        sum2.sort()

        return sum(sum2) - 2 * sum(sum2[:(len(nums) // 2)])
class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i,n):
                res += len(set(nums[i:j+1])) ** 2

        return res
        
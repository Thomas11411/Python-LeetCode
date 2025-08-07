class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = 10 ** 5 + 1
        for i in nums:
            if abs(res) > abs(i):
                res = i
            elif abs(res) == abs(i):
                res = max(res,i)

        return res
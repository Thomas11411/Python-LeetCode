class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        res = maxab = maxa = 0

        for i in nums:
            res = max(res, maxab * i)
            maxab = max(maxab, maxa - i)
            maxa = max(maxa, i)

        return res
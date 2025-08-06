class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_res = abs(sum(nums))
        pos = 0
        neg = 0

        for i in nums:
            if pos < 0:
                pos = 0
            if neg > 0:
                neg = 0
            pos += i
            neg += i
            max_res = max(max_res,pos,abs(neg))

        return max_res
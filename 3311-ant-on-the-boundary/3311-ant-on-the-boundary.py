class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        res = 0
        sum_ = 0

        for i in nums:
            sum_ += i
            if sum_ == 0:
                res += 1

        return res
        
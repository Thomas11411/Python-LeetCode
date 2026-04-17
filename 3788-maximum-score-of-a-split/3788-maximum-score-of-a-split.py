class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        r = nums.pop()
        l = sum_ - r
        res = l - r

        while len(nums) > 1:
            tmp_r = nums.pop()
            r = min(r, tmp_r)
            l -= tmp_r
            res = max(res, l - r)
        return res
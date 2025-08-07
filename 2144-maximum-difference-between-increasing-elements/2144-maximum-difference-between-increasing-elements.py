class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res , mn = -1 , float("Inf")
        for i,v in enumerate(nums):
            if i > 0:
                res = max(res,v - mn)
            mn = min(v,mn)
        return res if res > 0 else -1
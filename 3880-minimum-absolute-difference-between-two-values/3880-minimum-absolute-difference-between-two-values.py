class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        one, two = float("inf"), float("inf")
        res = float("inf")

        for i,v in enumerate(nums):
            if v == 0: continue
            elif v == 1: 
                one = i
                res = min(res, abs(one - two))
            else: 
                two = i
                res = min(res, abs(one - two))
                
        return -1 if res == float("inf") else res
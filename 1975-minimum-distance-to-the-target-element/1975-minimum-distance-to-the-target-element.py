class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 1000
        for i,v in enumerate(nums):
            if v == target:
                res = min(res,abs(i - start))
        return res
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i,v in Counter(nums).items():
            if v > 1:
                return i
        
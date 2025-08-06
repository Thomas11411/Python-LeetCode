from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final = 0
        for i,v in Counter(nums).items():
            if v == 1:
                final = i
        return final
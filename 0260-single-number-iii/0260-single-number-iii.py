from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        final = []
        for i,v in Counter(nums).items():
            if v == 1:
                final.append(i)
        return final
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        final = []
        for i,v in Counter(nums).items():
            if v == 2:
                final.append(i)
        return final
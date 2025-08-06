from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        final = []
        n = len(nums)
        for i,v in Counter(nums).items():
            if v > (n/3):
                final.append(i)
        return final
        
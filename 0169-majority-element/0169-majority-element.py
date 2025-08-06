from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        final = 0
        n = len(nums)
        for i,v in Counter(nums).items():
            if v > (n/2):
                final = i
        return final
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([i if v == 1 else 0 for i,v in Counter(nums).items()])  
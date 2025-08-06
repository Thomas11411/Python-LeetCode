from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i,v in sorted(Counter(arr).items(),key = lambda x: x[1],reverse = True):
            if v > (len(arr) / 4):
                return i
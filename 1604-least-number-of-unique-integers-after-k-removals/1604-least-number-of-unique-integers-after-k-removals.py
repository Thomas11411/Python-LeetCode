from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dct = {i: v for i, v in sorted(Counter(sorted(arr)).items(), key=lambda item: item[1])}
        count = len(dct)
        for i in dct.values():
            if k >= i:
                k -= i
                count -= 1
            else:
                return count
        return count
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dct = {i:v for i,v in sorted(Counter(arr).items(),key = lambda x : x[1])}
        dct_values = list(dct.values())
        n = len(arr)
        count = 0
        while n > len(arr)/2 :
            n -= dct_values.pop()
            count += 1
        return count
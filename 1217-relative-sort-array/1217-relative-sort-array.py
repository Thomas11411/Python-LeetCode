from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = {k: n for k, n in Counter(arr1).items()}
        final = []
        for i in arr2:
            final += [i] * arr1_count[i]
            del arr1_count[i]
        
        for j in sorted(list(arr1_count)):
            final += [j] * arr1_count[j]
            
        return final
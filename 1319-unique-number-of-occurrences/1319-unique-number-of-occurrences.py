from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(Counter(arr)) == len(set(Counter(arr).values())):
            return True
        else:
            return False
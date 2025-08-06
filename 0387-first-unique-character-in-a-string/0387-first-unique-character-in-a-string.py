class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        temp = Counter(s)

        for i,v in enumerate(s):
            if temp[v] == 1:
                return i
        return -1
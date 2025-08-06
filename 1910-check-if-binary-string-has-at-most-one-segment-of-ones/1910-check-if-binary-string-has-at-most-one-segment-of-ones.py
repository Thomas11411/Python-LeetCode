class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cut = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                cut += 1
            if cut == 2:
                return False
        return True
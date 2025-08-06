class Solution:
    def getSmallestString(self, s: str) -> str:
                
        s = list(s)

        for i in range(1,len(s)):
            if s[i - 1] > s[i] and (int(s[i - 1]) - int(s[i])) % 2 == 0:
                s[i - 1], s[i] = s[i], s[i - 1]
                return ''.join(s)
        return ''.join(s)
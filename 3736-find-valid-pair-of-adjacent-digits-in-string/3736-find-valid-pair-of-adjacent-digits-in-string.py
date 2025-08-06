class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter

        d = set(i for i in Counter(s) if Counter(s)[i] == int(i))

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]: continue
            if s[i] in d and s[i + 1] in d: return s[i:i+2]

        return ""
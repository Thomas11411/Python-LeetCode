class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(0, n, 2):
            res += (s[i] != s[i + 1])

        return res
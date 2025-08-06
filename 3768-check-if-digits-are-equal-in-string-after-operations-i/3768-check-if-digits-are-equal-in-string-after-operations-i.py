class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            n = len(s)
            for i in range(1, n):
                s += str((int(s[i - 1]) + int(s[i])) % 10)
            s = s[n:]

        return s[0] == s[1]
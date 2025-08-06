class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = cur = 0

        for r in range(1, len(s)):
            cur += (s[r - 1] == s[r])
            if cur > 1:
                l += 1
                cur -= (s[l - 1] == s[l])

        return len(s) - l
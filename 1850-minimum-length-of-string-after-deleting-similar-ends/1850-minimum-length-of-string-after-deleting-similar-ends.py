class Solution:
    def minimumLength(self, s: str) -> int:
        r = len(s) - 1
        l = 0
        while l < r and s[r] == s[l]:
            letter = s[l]
            while l <= r and s[l] == letter:
                l += 1
            while r > l and s[r] == letter:
                r -= 1

        return r - l + 1 
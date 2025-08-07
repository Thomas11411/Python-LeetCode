class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        s = list(s)
        for i in range(n // 2):
            
            sel = min(s[i], s[n - i - 1])
            s[i], s[n - i - 1] = sel, sel

        return ''.join(s)
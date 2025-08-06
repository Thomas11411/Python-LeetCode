class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        d = Counter(s)

        left = ""
        mid = ""

        for i in sorted(set(s)):
            left += i * (d[i] // 2)
            if d[i] % 2 == 1:
                mid = i
                
        return left + mid + left[::-1]
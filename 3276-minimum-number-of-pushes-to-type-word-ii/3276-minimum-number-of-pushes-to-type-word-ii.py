class Solution:
    def minimumPushes(self, word: str) -> int:

        from collections import Counter

        d = Counter(word)
        cnt = sorted(list(d.values()), reverse = True)
        n = len(cnt)

        quotient = n // 8
        remainder = n % 8

        ans = 0

        for i in range(quotient + 1):
            for j in cnt[(i * 8):((i + 1) * 8)]:
                ans += (i + 1) * j

        return ans
        
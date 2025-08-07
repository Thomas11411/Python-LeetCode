class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
        d = Counter(words)

        mid = False
        res = 0

        for i in set(words):
            if len(set(i)) != 1:
                if d[i] and d[i[::-1]]:
                    cnt = min(d[i],d[i[::-1]])
                    res += (cnt * 4)
                    d[i] -= cnt
                    d[i[::-1]] -= cnt

            else:
                if d[i] % 2 == 1:
                    mid = True
                res += (d[i] // 2) * 4
                d[i] %= 2


        return res + mid * 2
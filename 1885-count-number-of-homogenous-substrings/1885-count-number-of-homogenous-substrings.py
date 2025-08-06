class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 1
        res = 0
        mod = 10 ** 9 + 7

        for i in range(1,len(s)):
            if s[i - 1] == s[i]:
                count += 1

            else:
                res += ((1 + count) * count / 2)
                count = 1
                
        res += ((1 + count) * count / 2)

        return int(res % mod)
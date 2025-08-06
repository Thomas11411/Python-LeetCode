class Solution:
    def maxPower(self, s: str) -> int:
        res = [1] * len(s)
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                res[i] += res[i-1]
        return max(res)
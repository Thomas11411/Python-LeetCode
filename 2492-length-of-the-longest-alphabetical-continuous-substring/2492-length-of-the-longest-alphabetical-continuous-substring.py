class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        tmp = 1
        for i in range(1,len(s)):

            if ord(s[i]) - ord(s[i - 1]) == 1:
                tmp += 1
                res = max(res,tmp)
            else:
                tmp = 1
            

        return res
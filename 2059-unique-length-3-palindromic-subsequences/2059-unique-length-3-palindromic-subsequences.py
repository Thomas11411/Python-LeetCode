class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for i in set(s):
            l , r = s.index(i)+1 , s.rindex(i)
            res += len(set(s[l:r]))
        return res
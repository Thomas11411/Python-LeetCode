class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc_dict = {x:0 for x in "abc"}
        res = 0
        start = -1
        for i,v in enumerate(s):
            abc_dict[v] += 1
            while all(abc_dict.values()):
                res += len(s) - i
                start += 1
                abc_dict[s[start]] -= 1
        return res
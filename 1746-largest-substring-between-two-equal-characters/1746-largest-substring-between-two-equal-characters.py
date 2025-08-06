class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        s_dict = dict()
        for i,v in enumerate(s):
            if v in s_dict:
                s_dict[v].append(i)
                res = max(res,max(s_dict[v]) - min(s_dict[v]) - 1)
            else:
                s_dict[v] = [i]
        return res
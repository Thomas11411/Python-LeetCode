from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {i:v for i,v in Counter(s).items()}
        for x in t:
            if x in s_dict and s_dict[x] > 0:
                s_dict[x] -= 1
        return sum(s_dict.values())
        
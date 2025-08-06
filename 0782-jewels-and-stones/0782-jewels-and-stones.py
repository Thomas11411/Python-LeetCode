from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ct = {k: n for k, n in Counter(S).items()}
        final = 0
        for i in J:
            try:
                final += ct[i]
            except:
                continue
        return final
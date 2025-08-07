class Solution:
    def repeatedCharacter(self, s: str) -> str:
        from collections import defaultdict

        d = defaultdict(int)

        for i in s:
            d[i] += 1
            if d[i] == 2:
                return i
        return ""
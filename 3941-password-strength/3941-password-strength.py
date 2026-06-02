class Solution:
    def passwordStrength(self, password: str) -> int:
        from collections import Counter

        d = Counter()

        res = 0

        for i in password:
            if d[i] == 0:
                if i.islower():
                    res += 1
                elif i.isupper():
                    res += 2
                elif i.isnumeric():
                    res += 3
                elif i in {"!","@","#","$"}:
                    res += 5
                d[i] += 1
        return res
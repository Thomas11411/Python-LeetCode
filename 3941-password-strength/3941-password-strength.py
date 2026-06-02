class Solution:
    def passwordStrength(self, password: str) -> int:
        d = set()

        res = 0

        for i in set(password):
            if d not in d:
                if i.islower():
                    res += 1
                elif i.isupper():
                    res += 2
                elif i.isnumeric():
                    res += 3
                elif i in {"!","@","#","$"}:
                    res += 5
                d.add(i)
        return res
class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for i in s:
            if i == "*" and res:
                res.pop()
            elif i == "%":
                res = res[::-1]
            elif i == "#":
                res += res
            elif i.isalpha():
                res.append(i)

        return ''.join(res)
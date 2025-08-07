class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for i in s:
            if i != "*":
                res.append(i)
            elif i == "*" and res:
                res.pop()

        return ''.join(res)
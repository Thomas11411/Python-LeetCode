class Solution:
    def finalString(self, s: str) -> str:

        res = []

        for l in s:
            if l == "i":
                res = res[::-1]
            else:
                res.append(l)
                
        return ''.join(res)
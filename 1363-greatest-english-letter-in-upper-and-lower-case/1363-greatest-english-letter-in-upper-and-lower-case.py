class Solution:
    def greatestLetter(self, s: str) -> str:
        from collections import defaultdict

        d = defaultdict(list)

        res = ""

        for i in s:
            if not d[i.upper()]:
                d[i.upper()] = [False,False]

            if i.isupper():
                d[i.upper()][1] = True
            else:
                d[i.upper()][0] = True

            if all(d[i.upper()]):
                res = max(res,i.upper())
                
        return res
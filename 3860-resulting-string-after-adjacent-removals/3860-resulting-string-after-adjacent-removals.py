class Solution:
    def resultingString(self, s: str) -> str:
        from string import ascii_lowercase as alpha

        d = dict(zip(alpha, zip(alpha[1:] + 'a', 'z' + alpha[:-1])))
        res = []

        for i in s:
            if res and res[-1] in d[i]: res.pop()
            else: res.append(i)
                
        return ''.join(res)
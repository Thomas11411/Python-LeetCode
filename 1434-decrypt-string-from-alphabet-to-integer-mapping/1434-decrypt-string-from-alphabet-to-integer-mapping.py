class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        res = []
        while i <= len(s) - 1:
            if i <= len(s) - 3:
                if s[i + 2] == "#":
                    res.append(chr(ord("a") + (int(s[i:i+2])-1)))
                    i += 3
                else:
                    res.append(chr(ord("a") + (int(s[i])-1)))
                    i += 1
            else:
                res.append(chr(ord("a") + (int(s[i])-1)))
                i += 1
        return ''.join(res)
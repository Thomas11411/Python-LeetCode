class Solution:
    def makeGood(self, s: str) -> str:
        res = [s[0]]
        for i in range(1,len(s)):
            if res:
                if res[len(res)-1] == s[i].swapcase():        
                    res.pop()
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
        return ''.join(res)
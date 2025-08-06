class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        now = ""
        for i in s:
            
            if now == i:
                count += 1
                if count <= 2:
                    res.append(i)
                    
            else:
                now = i
                count = 1
                res.append(i)
        return ''.join(res)
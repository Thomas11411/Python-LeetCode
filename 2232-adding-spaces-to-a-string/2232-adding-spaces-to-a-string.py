class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        j = 0
        for i,v in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                res += " "
                j += 1
            res += v
    
        return ''.join(res)
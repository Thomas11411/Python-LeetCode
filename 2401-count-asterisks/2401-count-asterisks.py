class Solution:
    def countAsterisks(self, s: str) -> int:
        res , cnt = 0 , 0

        for i in s:
            if i == "|":
                cnt += 1
            elif i == "*" and cnt % 2 == 0:
                res += 1
                
        return res
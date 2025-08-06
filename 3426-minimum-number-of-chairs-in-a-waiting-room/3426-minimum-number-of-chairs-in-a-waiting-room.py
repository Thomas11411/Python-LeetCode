class Solution:
    def minimumChairs(self, s: str) -> int:

        res = 0
        tmp = 0

        for i in s:
            if i == "E": tmp += 1
            else: tmp -= 1
            
            res = max(res, tmp)

        return res
        
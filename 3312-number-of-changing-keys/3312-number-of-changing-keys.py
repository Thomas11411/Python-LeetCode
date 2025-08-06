class Solution:
    def countKeyChanges(self, s: str) -> int:
                
        n = len(s)
        res = 0
        s1 = s.upper()

        for i in range(1, n):
            if s1[i] != s1[i - 1]:
                res += 1

        return res
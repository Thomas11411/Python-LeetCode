class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0

        for i,v in enumerate(str(n)):
            if i % 2 == 0:
                res += int(v)
            else:
                res -= int(v)

        return res
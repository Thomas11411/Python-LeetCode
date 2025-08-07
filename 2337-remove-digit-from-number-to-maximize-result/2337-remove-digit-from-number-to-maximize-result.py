class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        res = "0"
        for i in range(len(number)):
            if number[i] == digit:
                c = list(number).copy()
                c.pop(i)
                res = max(res,''.join(c))

        return res
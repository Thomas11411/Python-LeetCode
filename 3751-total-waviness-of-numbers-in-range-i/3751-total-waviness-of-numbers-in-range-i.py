class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0

        for val in range(num1, num2 + 1):
            n = str(val)
            for a, b, c in zip(n, n[1:], n[2:]):
                res += (a > b < c or a < b > c)

        return res
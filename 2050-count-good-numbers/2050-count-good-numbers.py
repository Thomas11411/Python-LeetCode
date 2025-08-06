class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        four = int(n // 2)
        five = (n - four)
        count4 = pow(4,four,mod)
        count5 = pow(5,five,mod)
        ans = (count4 * count5) % mod

        return ans
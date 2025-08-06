class Solution:
    def numWays(self, s: str) -> int:
        all_one = [i for i in range(len(s)) if s[i] == '1']
        if len(all_one) % 3 != 0:
            return 0

        if not all_one and len(s) >= 3:
            return int((((len(s) - 1) * (len(s) - 2)) / 2 ) % (10 ** 9 + 7))
        elif not all_one and len(s) < 3:
            return 0

        res = 1
        for i in range(1,3):
            res *= all_one[(len(all_one) // 3) * i] - all_one[(len(all_one) // 3) * i - 1]

        return res % (10 ** 9 + 7)
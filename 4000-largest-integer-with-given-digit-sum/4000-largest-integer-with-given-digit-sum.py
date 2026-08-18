class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n: return -1

        res = 0

        for i in range(n - 1, -1, -1):
            cur = min(9, s)
            res += cur * 10 ** i
            s -= cur
            if s == 0:
                return res
        return res
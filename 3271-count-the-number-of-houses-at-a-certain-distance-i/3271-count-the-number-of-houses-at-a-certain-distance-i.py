class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:

        res = [0] * n

        x -= 1
        y -= 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                d = min(abs(i - j), abs(i - x) + abs(j - y) + 1, abs(i - y) + abs(j - x) + 1)
                res[d - 1] += 2

        return res
        
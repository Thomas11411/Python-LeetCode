class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        cnt = 1
        add = 0
        while sum(int(i) for i in str(n + add)) > target:
            add = ((n // (10 ** cnt) + 1) * (10 ** cnt)) - n
            cnt += 1

        return add
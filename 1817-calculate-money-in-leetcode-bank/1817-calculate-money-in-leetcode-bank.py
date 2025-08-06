class Solution:
    def totalMoney(self, n: int) -> int:
        return int(((sum(range(0,7)) * (n // 7)) + 0.5 * (1 + (n // 7)) * (n // 7) * 7) + (((n // 7) + 1) * (n % 7) + sum(range(0,(n % 7)))))
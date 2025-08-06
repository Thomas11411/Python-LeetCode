class Solution:
    def minimumPushes(self, word: str) -> int:

        n = len(word)

        quotient = n // 8
        remainder = n % 8

        return int((quotient + 1) * quotient / 2) * 8 + (quotient + 1) * remainder
        
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        return sum(map(int, str(x))) if x % sum(map(int, str(x))) == 0 else -1
        
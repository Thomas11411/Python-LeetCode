class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n_str = list(str(n))
        digitSum = sum(map(int, n_str))
        squareSum = sum(map(lambda x: int(x) ** 2, n_str))
        return squareSum - digitSum >= 50
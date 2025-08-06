class Solution:
    def checkDivisibility(self, n: int) -> bool:
        import math
        lst = list(map(int, str(n)))
        return n % (sum(lst) + math.prod(lst)) == 0
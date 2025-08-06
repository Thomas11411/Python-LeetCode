class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        from functools import reduce
        from operator import mul

        while True:
            if reduce(mul, map(int, str(n))) % t == 0: return n
            n += 1
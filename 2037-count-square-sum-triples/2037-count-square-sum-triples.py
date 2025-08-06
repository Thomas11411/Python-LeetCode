class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1,n-1):
            for b in range(a+1,n):
                c = (a ** 2 + b ** 2) ** 0.5
                if c > n:
                    break
                if c.is_integer() and c <= n:
                    res += 2
        return res
            
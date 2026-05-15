class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        import math

        def isprime(n):
            if n == 1:
                return False
            elif n == 2:
                return True
            elif n % 2 == 0:
                return False
            
            lim = int(math.sqrt(n)) + 1
            
            for i in range(3, lim, 2):
                if n % i == 0: return False
            return True
            


        rev = int(str(n)[::-1])

        mn, mx = min(rev, n), max(rev, n)
        res = 0

        for num in range(mn, mx + 1):
            if isprime(num): res += num

        return res
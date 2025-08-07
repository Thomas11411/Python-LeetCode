class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factor(n):
            i = 2
            tmp = set()
            while i ** 2 <= n:
                if n % i != 0:
                    i += 1
                else:
                    tmp.add(i)
                    n //= i 
            if n > 1:
                tmp.add(n)
            return tmp

        res = set()
        for i in nums:
            res.update(prime_factor(i))
            
        return len(res)
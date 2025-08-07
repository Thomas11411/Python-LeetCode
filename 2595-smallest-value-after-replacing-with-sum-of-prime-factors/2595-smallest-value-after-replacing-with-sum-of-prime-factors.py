class Solution:
    def smallestValue(self, n: int) -> int:
        def factor(n):
            i = 2
            tmp = []
            while (i ** 2) <= n:
                if n % i != 0:
                    i += 1
                else:
                    tmp.append(i)
                    n //= i
            if n > 1:
                tmp.append(n)
            return tmp

        seen = set()
        while True:
            tmp = factor(n)
            if len(tmp) == 1:
                return tmp[0]
                
            n = sum(tmp)
            
            if n in seen:
                return n
            
            seen.add(n)
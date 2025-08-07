class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def prime_factor2(n):
            if n == 1: return False
            i = 2
            while i ** 2 <= n:
                if n % i != 0:
                    i += 1
                else:
                    return False
            return True

        tmp = []
        cnt = float("inf")
        res = [-1,-1]

        for i in range(left, right+1):
            if prime_factor2(i):
                tmp.append(i)
                
            if len(tmp) == 2:
                if tmp[1] - tmp[0] < cnt:
                    res = [tmp[0],tmp[1]]
                    cnt = tmp[1] - tmp[0]
                    if cnt <= 2: return res
                tmp.pop(0)
                
        return res
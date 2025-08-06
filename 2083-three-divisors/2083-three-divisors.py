class Solution:
    def isThree(self, n: int) -> bool:
        res = set()
        for i in range(1,n+1):
            if n % i == 0:
                if i in res or n / i in res:
                    break
                res.add(i)
                res.add(n / i)
        return len(res) == 3
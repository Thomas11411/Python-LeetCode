class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        prime = [1] * (n + 1)
        prime[0] = prime[1] = 0

        p = 2

        while p ** 2 <= n:
            if prime[p]:
                for i in range(p ** 2, n + 1, p): prime[i] = 0
                    
            p += 1

        res = []
            
        for i in range(2, (n // 2) + 1):
            if prime[i] and prime[n - i]: res.append([i, n - i])

        return res
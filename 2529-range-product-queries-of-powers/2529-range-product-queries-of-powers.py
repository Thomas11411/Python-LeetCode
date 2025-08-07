class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        l = bin(n)[2:][::-1]

        arr = [1]
        cur = 1

        for i in range(len(l)):
            if l[i] == "1":
                cur *= (2 ** i)
                arr.append(cur)
                
        res = []
                
        for i,j in queries:
            res.append(int(arr[j+1] / arr[i]) % (10 ** 9 + 7))

        return res
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = [0] * n

        for i,j in roads:
            d[i] += 1
            d[j] += 1

        d.sort()
        res = 0

        for i,v in enumerate(d,start = 1):
            res += i * v

        return res
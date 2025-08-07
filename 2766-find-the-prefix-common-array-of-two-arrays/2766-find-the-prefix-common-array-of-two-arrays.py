class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        from collections import defaultdict

        d = defaultdict(int)
        cur = 0
        res = []

        for i in range(len(A)):
            d[A[i]] += 1
            d[B[i]] += 1
            cur += (d[A[i]] == 2) + (d[B[i]] == 2) - (A[i] == B[i])
            res.append(cur)

        return res
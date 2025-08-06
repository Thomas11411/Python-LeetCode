class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                res[r][c] = min(rowSum[r],colSum[c])
                rowSum[r] -= res[r][c]
                colSum[c] -= res[r][c]
        return res
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        res = matrix.copy()

        n = len(matrix)
        m = len(matrix[0])

        mx = [max(c) for c in zip(*matrix)]

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == -1: res[r][c] = mx[c]

        return res
        
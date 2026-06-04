class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda x: x[2], reverse = True)

        res = [[0] * m for i in range(n)]

        for i, j, v in sources:
            res[i][j] = v

        for i, j, v in sources:
            for d_i, d_j in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0 <= i + d_i < n and 0 <= j + d_j < m and res[i + d_i][j + d_j] == 0:
                    res[i + d_i][j + d_j] = v
                    sources.append([i + d_i, j + d_j, v])
        return res
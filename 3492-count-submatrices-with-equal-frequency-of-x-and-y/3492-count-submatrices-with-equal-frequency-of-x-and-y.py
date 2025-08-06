class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
                
        n = len(grid)
        m = len(grid[0])

        X = [[0] * (m + 1) for i in range(n + 1)]
        Y = [[0] * (m + 1) for i in range(n + 1)]

        res = 0

        for i in range(n):
            for j in range(m):
                X[i][j] = X[i-1][j] + X[i][j-1] - X[i-1][j-1] + (grid[i][j] == "X")
                Y[i][j] = Y[i-1][j] + Y[i][j-1] - Y[i-1][j-1] + (grid[i][j] == "Y")
                if X[i][j] > 0 and X[i][j] == Y[i][j]: res += 1

        return res
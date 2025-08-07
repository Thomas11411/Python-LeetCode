class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        res = [[0]*(n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))

        return res
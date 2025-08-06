class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] <= grid[i - 1][j]:
                    res += (grid[i - 1][j] - grid[i][j] + 1)
                    grid[i][j] = grid[i - 1][j] + 1

        return res
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(1,m-1):
            for j in range(1,n-1):
                ans = max(ans,sum(grid[i-1][(j-1):(j+2)]) + grid[i][j] + sum(grid[i+1][(j-1):(j+2)]))

        return ans
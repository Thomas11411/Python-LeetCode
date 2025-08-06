class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j] == 1: continue

                if i == 0 and j == 0: res[i][j] = 1
                if i > 0: res[i][j] += res[i-1][j]
                if j > 0: res[i][j] += res[i][j-1]
            




        return res[-1][-1]
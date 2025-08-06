class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for x in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j]:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                res += dp[i][j]
        return res
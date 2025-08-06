class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        out = 0
        dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    out = max(out, dp[i + 1][j + 1])

        return out
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            pts , skip = questions[i]
            dp[i] = max(pts + dp[min(i + skip + 1,n)],dp[i + 1])

        return dp[0]
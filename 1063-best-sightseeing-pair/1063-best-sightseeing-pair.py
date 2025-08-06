class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxAi, result = 0, 0
        for j in range(len(A)):
            result = max(maxAi+A[j]-j, result)
            maxAi = max(maxAi, A[j]+j)
        return result
        
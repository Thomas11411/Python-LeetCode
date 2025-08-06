class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        res = 0

        for i in range(len(maxHeights)):
            res = max(res, sum(accumulate(maxHeights[i::-1], min)) + sum(accumulate(maxHeights[i:], min)) -  maxHeights[i])

        return res
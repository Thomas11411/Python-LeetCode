class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        score = [sum(r) for r in grid]
        return score.index(max(score))
        
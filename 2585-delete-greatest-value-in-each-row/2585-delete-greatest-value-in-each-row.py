class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(max(j) for j in zip(*[sorted(i) for i in grid]))
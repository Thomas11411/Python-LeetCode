class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0

        for r in grid:
            for c in zip(*grid):
                if r == list(c):
                    res += 1

        return res
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        from itertools import pairwise
        for i, j in pairwise(grid[0]):
            if i == j: return False

        if any(len(i) != 1 for i in map(set, zip(*grid))): return False

        return True
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        from collections import Counter

        for i in range(2):
            for j in range(2):
                block = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
                d = list(Counter(block).values())
                if len(d) == 1 or d[0] != d[1]: return True
        return False
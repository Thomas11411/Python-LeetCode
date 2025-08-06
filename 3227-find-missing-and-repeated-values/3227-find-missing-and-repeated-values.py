class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        from collections import defaultdict

        n = len(grid) ** 2 
        d = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                d[grid[i][j]] += 1
                if d[grid[i][j]] == 2:
                    a = grid[i][j]
                    
        res = [a]
        res += list(set(range(1,n+1)) - set(d.keys()))

        return res
        
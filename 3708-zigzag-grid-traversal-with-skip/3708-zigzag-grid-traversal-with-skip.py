class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m = len(grid[0])
        n = len(grid)
        res = []

        for i in range(n):
            
            if i % 2 == 0: j_vec = range(0, m, 2)
            else: j_vec = [k for k in range(m - 1, -1, -1) if k % 2 == 1]
            
            for j in j_vec: res.append(grid[i][j])

        return res
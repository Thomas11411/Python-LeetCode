class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if not(0 <= r < m and 0 <= c < n and grid[r][c] != 0):
                return 0
            cnt = grid[r][c]
            grid[r][c] = 0
            for dr, dc in directions:
                cnt = (cnt + dfs(r + dr, c + dc)) % k
            return cnt

        return sum(dfs(r, c) == 0 for r in range(m) for c in range(n) if grid[r][c] != 0)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            
            # mark cell visited
            grid[i][j] = '#'
            
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
                    
        return ans
        
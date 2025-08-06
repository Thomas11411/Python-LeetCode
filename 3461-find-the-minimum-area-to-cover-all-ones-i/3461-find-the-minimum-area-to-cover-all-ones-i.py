class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
                
        r_loc = [float('inf'), float('-inf')]
        r_vec = list(map(lambda x: sum(x) != 0, grid))

        for r in range(len(grid)):
            if r_vec[r]:
                r_loc[0] = min(r_loc[0], r)
                r_loc[1] = max(r_loc[1], r)
                
        c_loc = [float('inf'), float('-inf')]
        c_vec = list(map(lambda x: sum(x) != 0, zip(*grid)))

        for c in range(len(grid[0])):
            if c_vec[c]:
                c_loc[0] = min(c_loc[0], c)
                c_loc[1] = max(c_loc[1], c)
                
                
        return (r_loc[1] - r_loc[0] + 1) * (c_loc[1] - c_loc[0] + 1)
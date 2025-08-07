class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        res = [[0] * len(grid[0]) for _ in range(len(grid))]

        c_cnt = len(grid[0])
        r_cnt = len(grid)

        r_data = list(map(lambda x: 2 * sum(x) - len(x), grid))
        c_data = list(map(lambda x: 2 * sum(x) - len(x), zip(*grid)))

        for r in range(r_cnt):
            for c in range(c_cnt):
                res[r][c] = r_data[r] + c_data[c]

        return res
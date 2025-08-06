class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        col_cnt = list(map(sum, zip(*grid)))
        row_cnt = list(map(sum, grid))
        res = 0

        for r in range(len(row_cnt)):
            for c in range(len(col_cnt)):
                if grid[r][c]: res += (row_cnt[r] - 1) * (col_cnt[c] - 1)

        return res
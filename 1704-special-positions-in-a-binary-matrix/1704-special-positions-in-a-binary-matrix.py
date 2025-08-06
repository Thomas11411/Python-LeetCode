class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [sum(r) for r in mat]
        col_sum = [sum([mat[r][c] for r in range(len(mat))]) for c in range(len(mat[0]))]
        res = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and row_sum[r] == 1 and col_sum[c] == 1:
                    res += 1
        return res
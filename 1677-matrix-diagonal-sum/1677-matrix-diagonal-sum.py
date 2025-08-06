class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        all_dict = set([(i,len(mat)-i-1) for i in range(len(mat))] + [(i,i) for i in range(len(mat))])
        res = 0
        for i,j in all_dict:
            res += mat[i][j]
        return res
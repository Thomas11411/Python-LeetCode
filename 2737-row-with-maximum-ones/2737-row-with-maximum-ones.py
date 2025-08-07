class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return max([[i,sum(mat[i])] for i in range(len(mat))], key = lambda x: x[1])
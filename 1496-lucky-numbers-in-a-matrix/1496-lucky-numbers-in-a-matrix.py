class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = list(map(lambda x : min(x),matrix))
        max_in_col = [max([matrix[i][y] for i in range(len(matrix))]) for y in range(len(matrix[0]))]
        return [ x for x in max_in_col if x in min_in_row]
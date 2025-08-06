class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([sum(map(lambda i : 1 if i < 0 else 0,j)) for j in grid])
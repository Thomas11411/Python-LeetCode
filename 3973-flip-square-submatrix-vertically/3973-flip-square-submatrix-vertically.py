class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            row1, row2 = grid[x + i], grid[x + k - i - 1]
            row1[y: y + k], row2[y: y + k] = row2[y: y + k] , row1[y: y + k] 
        return grid
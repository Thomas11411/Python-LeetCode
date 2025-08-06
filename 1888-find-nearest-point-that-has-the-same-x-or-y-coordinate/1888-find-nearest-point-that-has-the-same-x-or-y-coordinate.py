class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_len = float("inf")
        res = -1
        for i,j in enumerate(points):
            if (j[0] == x or j[1] == y) and abs(j[0] - x) + abs(j[1] - y) < min_len:
                min_len = abs(j[0] - x) + abs(j[1] - y)
                res = i

        return res
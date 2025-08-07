class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        new = []
        for row in grid:
            new += row
        new.sort()


        res = 0
        mid = new[len(new) // 2]
        for i in new:
            if abs(i - mid) % x != 0:
                return -1
            res += abs(i - mid) // x

        return res
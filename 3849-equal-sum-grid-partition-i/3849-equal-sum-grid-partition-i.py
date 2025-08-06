class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g):
            sum_ = 0
            for r in g:
                sum_ += sum(r)
                if (sum_ * 2) == total:
                    return True
            return False

        total = sum(sum(g) for g in grid)

        return check(grid) or check(zip(*grid))
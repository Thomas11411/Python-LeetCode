class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        return sum((total - j * cost2) // cost1 + 1 for j in range(total // cost2 + 1))
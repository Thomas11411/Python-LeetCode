class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        val, idx = float("Inf"), -1

        for i, v in enumerate(capacity):
            if itemSize <= v < val:
                val, idx = v, i
        return idx
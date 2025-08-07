class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0

        for i in sorted(c - r for c,r in zip(capacity,rocks)):
            if not additionalRocks or additionalRocks < i:
                return res
            else:
                res += 1
                additionalRocks -= i
        return res
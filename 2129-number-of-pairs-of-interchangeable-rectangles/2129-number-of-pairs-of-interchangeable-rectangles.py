class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        res = 0
        for i,j in rectangles:
            d[ i / j ] += 1
            if d[ i / j ] > 1:
                res += (d[ i / j ] - 1)

        return res
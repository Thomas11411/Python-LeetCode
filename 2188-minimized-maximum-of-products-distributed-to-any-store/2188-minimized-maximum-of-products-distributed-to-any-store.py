class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        import math
        s , e = 0 , max(quantities)

        while s + 1 < e:
            mid = (s + e) >> 1
            if sum(math.ceil(q / mid) for q in quantities) <= n:
                e = mid
            else:
                s = mid
        
        return e
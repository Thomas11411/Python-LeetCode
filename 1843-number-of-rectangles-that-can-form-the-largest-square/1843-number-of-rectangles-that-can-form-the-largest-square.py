class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        now_s = 0
        for l,w in rectangles:
            s = min(l,w)
            if s > now_s:
                now_s = s
                count = 1
            elif s == now_s:
                count += 1
        return count
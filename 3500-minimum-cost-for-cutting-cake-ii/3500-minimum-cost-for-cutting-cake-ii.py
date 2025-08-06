class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        import heapq

        d = [(-i, "H") for i in horizontalCut] + [(-i, "V") for i in verticalCut]

        heapq.heapify(d)

        v = 1; h = 1
        res = 0

        while d:
            c, s = heapq.heappop(d)
            if s == "H":
                res += (c * v)
                h += 1
            else:
                res += (c * h)
                v += 1

        return -res
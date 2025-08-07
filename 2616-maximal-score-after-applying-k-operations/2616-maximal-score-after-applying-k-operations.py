class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq

        sq = [-i for i in nums]
        heapq.heapify(sq)
        res = 0

        for i in range(k):
            res -= sq[0]
            heapq.heapreplace(sq, sq[0] // 3)

        return res
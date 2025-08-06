class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        piles_new = [- i for i in piles]
        heapq.heapify(piles_new)
        while k > 0:
            now = heapq.heappop(piles_new)
            heapq.heappush(piles_new, int((now - 1) / 2))
            k -= 1
        return -sum(piles_new)
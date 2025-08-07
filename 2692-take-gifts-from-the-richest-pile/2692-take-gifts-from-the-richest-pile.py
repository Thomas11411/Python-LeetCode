class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        import heapq

        gifts2 = [-i for i in gifts]
        heapq.heapify(gifts2)

        for i in range(k):
            heapq.heapreplace(gifts2, - int((-gifts2[0]) ** 0.5))
            
        return - sum(gifts2)
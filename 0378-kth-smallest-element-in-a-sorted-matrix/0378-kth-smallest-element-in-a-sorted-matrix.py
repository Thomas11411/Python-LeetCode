class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        arr = []
        for i in matrix: arr += i
        heapq.heapify(arr)
        for i in range(k): res = heapq.heappop(arr)
        return res
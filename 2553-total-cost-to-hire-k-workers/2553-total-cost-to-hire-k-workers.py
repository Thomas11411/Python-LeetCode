class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        from collections import deque
        import heapq

        l , r , res = [] , [] , 0
        costs = deque(costs)

        for _ in range(k):
            while len(l) < candidates:
                heapq.heappush(l, costs.popleft() if costs else 100001)
            while len(r) < candidates:
                heapq.heappush(r, costs.pop() if costs else 100001)
                
            res += (heapq.heappop(l) if l[0] <= r[0] else heapq.heappop(r))

        return res
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        import heapq

        new = [- i for i in amount if i > 0]
        heapq.heapify(new)

        res = 0

        while len(new) > 1:
            first = heapq.heappop(new)
            second = heapq.heappop(new)
            first += 1
            second += 1
            res += 1
            if first:
                heapq.heappush(new,first)
            if second:
                heapq.heappush(new,second)

        if new:
            return res - new[0]

        else:
            return res

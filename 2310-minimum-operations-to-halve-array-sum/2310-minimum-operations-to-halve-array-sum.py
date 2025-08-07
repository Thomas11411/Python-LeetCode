class Solution:
    def halveArray(self, nums: List[int]) -> int:
        import heapq

        new = [-i for i in nums]
        heapq.heapify(new)

        sum_ = sum(new)
        half = sum_ / 2

        res = 0

        while sum_ < half:

            now = heapq.heappop(new) / 2
            sum_ -= now
            heapq.heappush(new, now)
            res += 1
            
        return res
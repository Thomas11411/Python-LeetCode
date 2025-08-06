class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        import heapq
        l = []
        heapq.heapify(l)

        for i in nums:
            heapq.heappush(l, -int(i))


        while k > 0:
            now = heapq.heappop(l)
            k -= 1
        return str(-now)

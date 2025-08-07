class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:

        import heapq

        heapq.heapify(nums)

        while k > 0:
            now = heapq.heappop(nums)
            heapq.heappush(nums,now+1)
            k -= 1

        res = 1
        for i in nums:
            res *= i
            res = res % ( 10 ** 9 + 7 ) 

        return res
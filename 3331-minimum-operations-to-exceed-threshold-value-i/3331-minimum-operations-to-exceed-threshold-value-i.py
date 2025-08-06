class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
                
        import heapq

        heapq.heapify(nums)
        res = 0

        while nums:
            cur = heapq.heappop(nums)
            if cur >= k:
                return res
                
            res += 1

        return res
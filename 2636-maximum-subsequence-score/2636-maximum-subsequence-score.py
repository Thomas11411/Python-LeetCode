class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq

        res = 0
        total = 0
        tmp = []
        heapq.heapify(tmp)

        for n1,n2 in sorted(zip(nums1,nums2),key = lambda x: -x[1]):

            if len(tmp) == k:
                total -= heapq.heappop(tmp)
            
            heapq.heappush(tmp,n1)
            total += n1
        
            if len(tmp) == k:
                res = max(res, total * n2)

        return res
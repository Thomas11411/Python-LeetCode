class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        import heapq
        diff = [-abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        k = k1 + k2
        if -sum(diff) <= k: return 0
        heapq.heapify(diff)

        while k and diff:
            top = -heapq.heappop(diff)
            delta  = max(k // len(nums1),  1) 
            heapq.heappush(diff, -(top - delta))
            k -= delta

        return sum(ii ** 2 for ii in diff)

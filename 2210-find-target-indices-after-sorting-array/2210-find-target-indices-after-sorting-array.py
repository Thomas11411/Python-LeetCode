class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        import heapq
        heapq.heapify(nums)
        res = []
        idx = -1
        while nums:
            idx += 1
            now = heapq.heappop(nums)
            if now == target:
                res.append(idx)
        return res
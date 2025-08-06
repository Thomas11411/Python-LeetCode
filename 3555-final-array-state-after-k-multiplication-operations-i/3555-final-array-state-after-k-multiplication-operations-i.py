class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq

        nums2 = list(zip(nums, range(len(nums))))

        heapq.heapify(nums2)

        while k > 0:
            v, i = heapq.heappop(nums2)
            v *= multiplier
            heapq.heappush(nums2, (v,i))
            k -= 1
            
        nums2 = sorted(nums2, key = lambda x: x[1])

        return list(zip(*nums2))[0]
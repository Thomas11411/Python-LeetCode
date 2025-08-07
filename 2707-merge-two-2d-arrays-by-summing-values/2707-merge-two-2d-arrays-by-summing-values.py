class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        nums = nums1 + nums2

        d = defaultdict(int)

        for i,v in nums:
            d[i] += v
            
        return sorted(d.items())
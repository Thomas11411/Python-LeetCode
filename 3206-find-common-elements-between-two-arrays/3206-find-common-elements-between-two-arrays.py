class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        c1 = sum(1 for v1 in nums1 if v1 in set2)
        c2 = sum(1 for v2 in nums2 if v2 in set1)

        return [c1, c2]

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        if set(nums1) & set(nums2): return min(set(nums1) & set(nums2))

        n1 = min(nums1)
        n2 = min(nums2)

        return n1 * 10 + n2 if n1 < n2 else n2 * 10 + n1
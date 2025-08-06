class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = sum(max(1,i) for i in nums1)
        s2 = sum(max(1,j) for j in nums2)

        if s1 > s2 and nums2.count(0) == 0: return -1
        if s1 < s2 and nums1.count(0) == 0: return -1

        return max(s1,s2)
        
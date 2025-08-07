class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        tmp = list(set(nums2) & set(nums1))

        return -1 if len(tmp) == 0 else min(tmp)
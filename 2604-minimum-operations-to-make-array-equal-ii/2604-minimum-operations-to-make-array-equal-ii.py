class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if nums1 == nums2: return 0

        if k == 0: return -1

        bal = 0
        res = 0

        for n1,n2 in zip(nums1,nums2):
            diff = n1 - n2
            cnt = diff // k
            
            if diff % k != 0:
                return -1
            
            bal += cnt
            res += abs(cnt)
            
        return res // 2 if bal == 0 else -1
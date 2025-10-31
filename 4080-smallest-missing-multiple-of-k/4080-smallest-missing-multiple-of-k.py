class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        cur = 0
        while True:
            cur += k
            if(cur not in nums): return cur
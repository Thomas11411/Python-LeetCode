class Solution:
    def specialArray(self, nums: List[int]) -> int:
        now = [sum([i >= j for i in nums]) == j for j in range(1,len(nums)+1)]
        for k,v in enumerate(now,start=1):
            if v:
                return k
        return -1
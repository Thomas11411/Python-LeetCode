class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def check(v):
            idx = [i for i, u in enumerate(nums) if u == v]
            return len(idx) % 2 == 0 and sum(idx[1::2]) - sum(idx[::2]) <= k
        return check(-1) or check(1)
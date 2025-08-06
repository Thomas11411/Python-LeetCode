class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        before = 0
        for i in rungs:
            diff = i - before - 1
            res += diff // dist
            before = i
        return res
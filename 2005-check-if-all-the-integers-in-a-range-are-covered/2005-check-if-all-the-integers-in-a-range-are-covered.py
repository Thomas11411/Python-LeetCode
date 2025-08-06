class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s1 = set(i for i in range(left, right+1))
        s2 = set(i for l,r in ranges for i in range(l, r+1))
        return s1.intersection(s2) == s1 
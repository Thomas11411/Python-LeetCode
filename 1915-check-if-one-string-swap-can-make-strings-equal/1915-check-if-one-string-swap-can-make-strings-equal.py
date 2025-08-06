class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s2 == s1: return True
        if sum([1 for i,j in zip(s1,s2) if i != j]) == 2 and set(s1) == set(s2): return True
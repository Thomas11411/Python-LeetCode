class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
                
        cnt = s.count(c)
        return int( (1 + cnt) * cnt / 2 )
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in words:
            if s[0:len(i)] == i:
                res += 1
        return res
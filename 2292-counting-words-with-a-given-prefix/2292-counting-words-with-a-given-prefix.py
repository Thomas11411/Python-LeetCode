class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(i[0:len(pref)] == pref for i in words)
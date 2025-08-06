class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        i = 0
        if len(word) == 1: return 1

        for j in range(1, len(word)):
            if word[j - 1] != word[j]:
                res += (j - i - 1)
                i = j
        return res + (j - i) + 1
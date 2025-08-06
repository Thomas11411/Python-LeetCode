class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        new = text.split(" ")
        res = len(new)
        for i in new:
            for j in i:
                if j in brokenLetters:
                    res -= 1
                    break
        return res
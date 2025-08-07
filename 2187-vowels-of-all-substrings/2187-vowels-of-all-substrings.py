class Solution:
    def countVowels(self, word: str) -> int:
        now , res = 0 , 0
        for i,l in enumerate(word):
            if l in "aeiou":
                now = i + 1 + (now if now else 0)
                res += now
            else:
                res += now

        return res
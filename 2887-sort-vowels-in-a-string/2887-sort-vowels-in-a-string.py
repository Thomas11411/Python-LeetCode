class Solution:
    def sortVowels(self, s: str) -> str:

        vow = sorted([i for i in s if i in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}])

        res = ""

        for i in s:
            if i not in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                res += i
            else:
                res += vow.pop(0)
                
        return res
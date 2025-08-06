class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for i in range(len(s)):
            if s[i] in vowel:
                if i < len(s)/2:
                    count += 1
                else:
                    count -= 1
        return True if count == 0 else False
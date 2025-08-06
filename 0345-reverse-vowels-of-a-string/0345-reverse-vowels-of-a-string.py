class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["A","E","I","O","U","a","e","i","o","u"]
        l , r = 0 , len(s) - 1
        s = list(s)
        while r > l:
            if s[r] in vowel and s[l] not in vowel:
                while s[l] not in vowel:
                    l += 1
                s[r] , s[l] = s[l] , s[r]
            elif s[r] not in vowel and s[l] in vowel:
                while s[r] not in vowel:
                    r -= 1
                s[r] , s[l] = s[l] , s[r]
            elif s[r] in vowel and s[l] in vowel:
                s[r] , s[l] = s[l] , s[r]

            r -= 1
            l += 1
        return ''.join(s)
        
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import defaultdict

        lower_d = defaultdict(int)
        upper_d = defaultdict(int)

        res = 0

        for i in word:
            if i.islower():
                lower_d[i] = 1 - upper_d[i]
            else:
                upper_d[i.lower()] = 1
                
                
        return sum(lower_d[i] * upper_d[i] for i in set(word.lower()))
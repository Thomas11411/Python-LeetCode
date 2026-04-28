class Solution:
    def sortVowels(self, s: str) -> str:
        from collections import defaultdict

        d = defaultdict(int)

        for i in s:
            if i in {"a", "e", "i", "o", "u"}: d[i] += 1

        d = sorted(d.items(), key = lambda x: x[1], reverse=True)
        all_vowel = ''.join([i * v for i,v in d])
        vowel_cnt = 0
        res = ""

        for i in s:
            if i in {"a", "e", "i", "o", "u"}:
                res += all_vowel[vowel_cnt]
                vowel_cnt += 1
            else:
                res += i
        return res
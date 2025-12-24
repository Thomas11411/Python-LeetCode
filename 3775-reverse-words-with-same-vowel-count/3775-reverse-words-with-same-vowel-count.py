class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split(" ")
        cnt = lambda x: sum(1 for i in x if i in {"a", "e", "i", "o", "u"})
        scale = cnt(new_s[0])

        for i in range(1, len(new_s)):
            if cnt(new_s[i]) == scale:
                new_s[i] = new_s[i][::-1]

        return ' '.join(new_s)
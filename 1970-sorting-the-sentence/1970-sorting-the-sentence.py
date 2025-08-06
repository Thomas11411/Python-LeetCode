class Solution:
    def sortSentence(self, s: str) -> str:
        res = [0] * len(s.split())
        for i in s.split():
            res[int(i[-1])-1] = i[:-1]
        return ' '.join(res)
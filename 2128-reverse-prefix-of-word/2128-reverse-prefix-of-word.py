class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = []
        been = False
        for i in word:
            res.append(i)
            if i == ch and not been:
                res = res[::-1]
                been = True
        return ''.join(res)
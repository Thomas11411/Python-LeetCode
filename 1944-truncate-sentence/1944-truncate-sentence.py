class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0
        res = []
        for i in s:
            if i == " ":
                count += 1
            if count == k:
                return ''.join(res)
            res.append(i)
        return ''.join(res)
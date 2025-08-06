class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)

        n1 = len(word1)
        n2 = len(word2)

        res = []

        while n2 > 0 or n1 > 0:
            if word1 >= word2:
                res.append(word1.pop(0))
                n1 -= 1
            else:
                res.append(word2.pop(0))
                n2 -= 1

        return ''.join(res)
            
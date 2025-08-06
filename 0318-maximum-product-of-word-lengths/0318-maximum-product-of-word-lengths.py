class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        words = sorted(words,key = lambda x : len(x),reverse=True)
        for i in range(len(words)-1):
            for j in range(i,len(words)):
                if len(words[i]) * len(words[j]) < res:
                    break
                if not set(words[i]) & set(words[j]):
                    res = max(res,(len(words[i]) * len(words[j])))
        return res
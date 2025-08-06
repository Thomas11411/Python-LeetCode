class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        T = [False] * (len_s + 1)
        T[0] = True
    
        for i in range(len_s):
            for j in range(i + 1, len_s + 1):
                if T[i] == True and s[i: j] in wordDict:
                    T[j] = True
        return T[~0]
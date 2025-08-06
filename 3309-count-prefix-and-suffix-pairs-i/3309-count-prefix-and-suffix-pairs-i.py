class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
                
        res = 0
        n = len(words)

        for i in range(n - 1):
            for j in range(i + 1, n):
                l = len(words[i])
                if words[j][-l:] == words[i] and words[j][:l] == words[i]:
                    res += 1

        return res
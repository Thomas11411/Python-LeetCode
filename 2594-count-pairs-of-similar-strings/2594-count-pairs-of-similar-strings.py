class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if set(words[i]) == set(words[j]):
                    res += 1

        return res
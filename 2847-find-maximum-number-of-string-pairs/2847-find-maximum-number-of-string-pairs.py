class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        res = 0

        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    res += 1
                    break

        return res
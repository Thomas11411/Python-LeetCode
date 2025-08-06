class Solution:
    def minTimeToType(self, word: str) -> int:
        word = "a" + word
        res = 0
        for i in range(1,len(word)):
            if word[i - 1] <= word[i]:
                res += min(ord(word[i]) - ord(word[i - 1]), 26 - ord(word[i]) + ord(word[i - 1])) + 1
            else:
                res += min(ord(word[i - 1]) - ord(word[i]), 26 - ord(word[i - 1]) + ord(word[i])) + 1

        return res
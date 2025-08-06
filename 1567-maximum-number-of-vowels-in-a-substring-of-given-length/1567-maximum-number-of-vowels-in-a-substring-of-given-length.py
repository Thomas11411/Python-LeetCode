class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dct = {"a","e","i","o","u"}
        count = 0
        for i in range(k):
            if s[i] in dct:
                count += 1
        max_count = count
        for j in range(0,len(s)-k):

            if s[j] in dct:
                count -= 1
            if s[j+k] in dct:
                count += 1
            max_count = max(max_count,count)
        return max_count
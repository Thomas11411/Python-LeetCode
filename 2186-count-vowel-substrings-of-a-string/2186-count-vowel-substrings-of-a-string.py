class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        return sum(set(word[i:j]) == set('aeiou') for i in range(0,len(word) - 4) for j in range(i + 5,len(word)+1)) 
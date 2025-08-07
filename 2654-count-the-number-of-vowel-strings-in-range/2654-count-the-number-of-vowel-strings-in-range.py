class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = {"a","e","i","o","u"}

        return sum([words[idx][0] in vowel and words[idx][-1] in vowel for idx in range(left,right+1)])
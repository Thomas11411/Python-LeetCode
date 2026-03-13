class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        cw = lambda ch: weights[ord(ch) - ord("a")]
        ww = lambda word: chr(ord("z") - sum(map(cw, word)) % 26)
        return ''.join(map(ww, words))
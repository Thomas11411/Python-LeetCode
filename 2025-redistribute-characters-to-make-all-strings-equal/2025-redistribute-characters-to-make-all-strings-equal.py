class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter

        return all(not i%len(words) for i in Counter("".join(words)).values())
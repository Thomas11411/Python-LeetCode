from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        charCounter = Counter(A[0])
        final = []
        for i in A[1:]:
            charCounter = charCounter & Counter(i)

        for i , v in charCounter.items():
            final.extend([i] * (v))
        return final
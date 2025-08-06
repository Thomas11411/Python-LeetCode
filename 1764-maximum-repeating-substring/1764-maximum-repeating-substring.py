class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(len(sequence) // len(word),-1,-1):
            if word * i in sequence:
                return i
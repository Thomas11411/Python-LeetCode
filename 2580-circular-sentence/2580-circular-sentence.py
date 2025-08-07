class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        word = sentence.split()

        for i in range(len(word)):
            if word[i][0] != word[i - 1][-1]:
                return False
        return True
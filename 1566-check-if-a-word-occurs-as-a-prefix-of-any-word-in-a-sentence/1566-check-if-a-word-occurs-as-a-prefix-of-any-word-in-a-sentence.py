class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        for i,v in enumerate(sentence):
            if searchWord == v[0:len(searchWord)]:
                return i+1
        return -1        
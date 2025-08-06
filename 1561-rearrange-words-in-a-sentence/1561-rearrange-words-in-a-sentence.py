class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text2 = text.split(" ")
        text2.sort(key=lambda x : len(x))
        text2 = " ".join(text2)
        return text2.capitalize()
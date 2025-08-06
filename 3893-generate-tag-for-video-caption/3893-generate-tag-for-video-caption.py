class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split(" ")
        res = "#"
        leave = 99

        for i, word in enumerate(words):
            if leave <= 0: break 
            n = min(leave, len(word))
            leave -= n
            tmp = ''.join([word[ii].lower() for ii in range(n) if word[ii].isalpha()])
            if not tmp: continue
            
            if res != "#":
                tmp = tmp.capitalize()
                
            res += tmp

        return res
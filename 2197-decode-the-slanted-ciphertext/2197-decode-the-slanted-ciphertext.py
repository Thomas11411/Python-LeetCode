class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        res = []
        for now in range(cols):
            i , j = 0 , now
            while (i * cols) + j < len(encodedText):
                res.append(encodedText[(i * cols) + j])
                i += 1
                j += 1
        return ''.join(res).rstrip()
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        isBlack = lambda x: (ord(x[0]) + int(x[1])) %2 == 0

        return isBlack(coordinate1) == isBlack(coordinate2)  
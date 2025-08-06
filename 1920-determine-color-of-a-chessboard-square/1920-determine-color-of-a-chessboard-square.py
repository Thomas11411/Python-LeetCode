class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        first = ord(coordinates[0]) - ord('a') + 1
        second = int(coordinates[1])
        
        if first % 2 == 0 and second % 2 == 1:
            return True
        elif first % 2 == 1 and second % 2 == 0:
            return True
        else:
            return False
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        res = 0

        minute = 60 * (int(correct[0:2]) - int(current[0:2])) + int(correct[3:5]) - int(current[3:5])

        if minute >= 60:
            res += minute // 60
            minute %= 60
        if minute >= 15:
            res += minute // 15
            minute %= 15
        if minute >= 5:
            res += minute // 5
            minute %= 5
        if minute >= 1:
            res += minute

        return res
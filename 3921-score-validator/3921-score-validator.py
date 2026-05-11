class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        res = [0, 0]

        for i in events:
            if i == "WD" or i == "NB":
                res[0] += 1
            elif i == "W":
                res[1] += 1
                if res[1] == 10: return res
            else:
                res[0] += int(i)
        return res
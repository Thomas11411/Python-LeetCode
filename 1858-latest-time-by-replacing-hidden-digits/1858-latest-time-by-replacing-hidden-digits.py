class Solution:
    def maximumTime(self, time: str) -> str:
        res = [None] * len(time)

        for i in range(len(time)):
            if time[i] != "?":
                res[i] = time[i]
            else:
                if i == 0 and time[i] == "?":
                    if time[i+1] == "?" or int(time[i+1]) <= 3:
                        res[i] = "2"
                    else:
                        res[i] = "1"

                if i == 1 and time[i] == "?":
                    if res[i-1] == "2":
                        res[i] = "3"
                    else:
                        res[i] = "9"

                if i == 3 and time[i] == "?":
                    res[i] = "5"

                if i == 4 and time[i] == "?":
                    res[i] = "9"
        return ''.join(res)
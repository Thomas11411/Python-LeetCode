class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st = startTime.split(":")
        et = endTime.split(":")

        second = lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
        return second(et) - second(st)
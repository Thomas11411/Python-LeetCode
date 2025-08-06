class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for d,s in zip(dist,speed):
            time.append(d/s)

        time.sort()
        for t in range(len(time)):
            arrive = (time[t] - t) <= 0
            if arrive:
                return t
        return len(time)

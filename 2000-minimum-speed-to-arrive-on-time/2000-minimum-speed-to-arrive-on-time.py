class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low = 1
        high = 10 ** 7 + 1

        def invalid(speed):
            time = 0

            for d in range(len(dist)-1):
                time += math.ceil(dist[d] / speed)
                if time > hour:
                    return False

            time += (dist[-1] / speed)

            return time <= hour

        res = -1
        while low <= high:
            now = (low + high) >> 1
            if invalid(now):
                res = now
                high = now - 1
            else:
                low = now + 1

        return res
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()

        r = time[0] * totalTrips
        l = 1

        while l < r:
            mid = l + (r - l) // 2
            if sum(mid // i for i in time) >= totalTrips:
                r = mid 
            else:
                l = mid + 1

        return l
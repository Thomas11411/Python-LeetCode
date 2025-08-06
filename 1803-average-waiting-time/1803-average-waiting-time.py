class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = []
        now = 0
        for a,t in customers:
            if a > now:
                wait.append(t)
                now = a + t
            else:
                wait.append(now - a + t)
                now += t
        return round(sum(wait) / len(wait),5)
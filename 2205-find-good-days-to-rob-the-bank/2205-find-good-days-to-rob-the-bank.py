class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        l , r = [1] , [1]
        n = len(security)

        now = 1
        for i in range(1,n):

            if security[i] <= security[i - 1]:
                now += 1
            else:
                now = 1

            l.append(now)

        now = 1
        for i in range(n - 2, -1 , -1):

            if security[i] <= security[i + 1]:
                now += 1
            else:
                now = 1

            r.append(now)

        r.reverse()

        return [i for i in range(n) if l[i] >= time + 1 and r[i] >= time + 1]
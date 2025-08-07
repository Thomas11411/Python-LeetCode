class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        start , end = [] , []
        for s , e , v in events:
            start.append((s,v))
            end.append((e,v))

        start.sort()
        end.sort()

        res , val , e = 0 , 0 , 0
        for s , v in start:

            while end[e][0] < s:
                val = max(val,end[e][1])
                e += 1

            res = max(res,val + v)

        return res
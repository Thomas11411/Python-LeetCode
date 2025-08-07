class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        presum = []
        count = 0
        left = []
        l_now = -1
        right = [0] * len(s)
        r_now = len(s)

        for i,v in enumerate(s):
            if v == "*":
                count += 1
            else:
                l_now = i
            left.append(l_now)
            presum.append(count)

        for i in range(r_now-1,-1,-1):
            if s[i] == "|":
                r_now = i
            right[i] = r_now

        res = []
        for a,b in queries:
            x , y = right[a] , left[b]
            if x <= y:
                res.append(presum[y] - presum[x])
            else:
                res.append(0)

        return res
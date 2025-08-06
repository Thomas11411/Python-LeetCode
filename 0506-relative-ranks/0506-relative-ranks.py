class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [0] * len(score)
        for x,y in enumerate(sorted([(i,v) for i,v in enumerate(score)],key = lambda x:x[1],reverse=True), start=1):
            if x == 1:
                res[y[0]] = "Gold Medal"
            elif x == 2:
                res[y[0]] = "Silver Medal"
            elif x == 3:
                res[y[0]] = "Bronze Medal"
            else:
                res[y[0]] = str(x)
        return res
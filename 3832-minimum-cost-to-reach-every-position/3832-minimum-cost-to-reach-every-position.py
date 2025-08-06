class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
                
        res = [cost[0]]

        for i in range(1, len(cost)):
            if res[-1] >= cost[i]:
                res.append(cost[i])
            else:
                res.append(res[-1])

        return res
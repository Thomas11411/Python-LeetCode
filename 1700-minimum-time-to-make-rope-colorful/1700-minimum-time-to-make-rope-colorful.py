class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i , res = 0 , 0
        while i < len(s):
            now , max_cost = cost[i] , cost[i]
            while i < len(s)-1 and s[i] == s[i+1]:
                now += cost[i+1]
                max_cost = max(max_cost,cost[i+1])
                i += 1
            res += (now - max_cost)
            i += 1
        return res
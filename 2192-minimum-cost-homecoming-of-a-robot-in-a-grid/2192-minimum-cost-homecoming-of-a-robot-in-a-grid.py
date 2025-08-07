class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        RL_dir = 1 if homePos[0] - startPos[0] > 0 else -1
        UD_dir = 1 if homePos[1] - startPos[1] > 0 else -1 

        res = 0

        for i in range(startPos[0],homePos[0],RL_dir):
            res += rowCosts[i + RL_dir]

        for j in range(startPos[1],homePos[1],UD_dir):
            res += colCosts[j + UD_dir]

        return res
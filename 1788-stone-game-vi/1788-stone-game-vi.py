class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        score = sorted([(aliceValues[i] + bobValues[i],i) for i in range(len(aliceValues))],reverse = True)

        a , b = 0 , 0
        for i,(v,score_idx) in enumerate(score):
            if i % 2 == 0:
                a += aliceValues[score_idx]
            else:
                b += bobValues[score_idx]
        
        if a == b: return 0
        return 1 if a > b else -1
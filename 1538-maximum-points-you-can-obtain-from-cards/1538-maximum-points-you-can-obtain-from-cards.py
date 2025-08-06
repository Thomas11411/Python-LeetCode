class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total
        miss = sum(cardPoints[:-k])
        ans = total - miss
        for i in range(k):
            miss = miss - cardPoints[i] + cardPoints[-(k-i)]
            ans = max(ans,total-miss)    
            
        return ans
        
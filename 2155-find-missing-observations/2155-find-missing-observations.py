class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l = len(rolls) + n
        now = mean * l - sum(rolls)
        
        if now > 6 * n or now < 1 * n:
            return []
        
        return [(now // n) + 1 if i <= now % n else now // n for i in range(1,n+1)]
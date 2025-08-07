class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = -1
        banned = set(banned)

        for i in range(1,n+1):
            if i not in banned:
                maxSum -= i
                res += 1
                
            if maxSum < 0:
                return res
            
        return res + 1
class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(x) for x in s]
        left = 1 - s[0]
        right = sum(s[1:])
        total = left + right
        for i in range(1,len(s)-1):
            left +=  (1 - s[i])
            right -= s[i]
            total = max(total,left + right)
        return total
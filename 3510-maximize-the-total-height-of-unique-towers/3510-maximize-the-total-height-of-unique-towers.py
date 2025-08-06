class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse = True)
        res = 0
        cur = float('inf')

        for m in maximumHeight:
            cur = min(cur - 1, m)
            if cur == 0: return -1
            res += cur
            
        return res